import re

import ollama


class LLMEngine:
    def __init__(self):
        self.model = "llama3.1"
        print("LLM Engine ready!")

    def _normalize_text(self, text):
        return re.sub(r"\s+", " ", text or "").strip()

    def _extract_relevant_snippet(self, context, query):
        text = self._normalize_text(context)
        query_terms = [term.lower() for term in re.findall(r"[A-Za-z0-9]+", query) if len(term) > 2]

        if not text:
            return ""

        sentences = [part.strip() for part in re.split(r"(?<=[.!?])\s+", text) if part.strip()]
        if not sentences:
            return text[:400]

        scored = []
        for sentence in sentences:
            sentence_lower = sentence.lower()
            score = sum(1 for term in query_terms if term in sentence_lower)
            if score == 0:
                score = 1 if any(term in sentence_lower for term in ("homework", "worksheet", "meeting", "class", "teacher", "parent", "assignment", "notice")) else 0
            scored.append((score, sentence))

        scored.sort(key=lambda item: item[0], reverse=True)
        top = [sentence for _, sentence in scored[:2] if sentence]
        return " ".join(top) if top else sentences[0]

    def _fallback_answer(self, context, query, role):
        safe_context = self._normalize_text(context)
        if not safe_context or "No relevant documents found." in safe_context:
            return "I do not have enough information in the uploaded document(s) to answer that question safely."

        snippet = self._extract_relevant_snippet(context, query)
        if snippet:
            return (
                f"I can answer only from the uploaded content. Relevant text: {snippet}"
            )
        return "I do not have enough information in the uploaded document(s) to answer that question safely."

    def generate_response(self, context, query, role):
        prompt = f"""You are EduBridge AI for early childhood education.
You are responding to a {role}.

IMPORTANT RULES:
- ONLY use information from the context below
- If context is empty or irrelevant, say exactly: I do not have enough information in the uploaded document(s) to answer that question safely.
- Do NOT make up or assume any information
- Be specific and accurate

Context:
{context}

Question: {query}

Response:"""

        try:
            response = ollama.chat(
                model=self.model,
                messages=[{"role": "user", "content": prompt}]
            )
            answer = response.get('message', {}).get('content', '').strip()
            if answer:
                return answer
        except Exception:
            pass

        return self._fallback_answer(context, query, role)

    def test(self):
        response = ollama.chat(
            model=self.model,
            messages=[{
                "role": "user",
                "content": "Say: EduBridge AI is ready!"
            }]
        )
        return response['message']['content']

if __name__ == "__main__":
    engine = LLMEngine()
    print(engine.test())