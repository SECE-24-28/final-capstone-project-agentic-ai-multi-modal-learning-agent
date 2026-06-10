from core.llm_engine import LLMEngine
from core.rag_pipeline import RAGPipeline

class EduAgent:
    def __init__(self):
        self.llm = LLMEngine()
        self.rag = RAGPipeline()

    def ask(self, query, role):
        context = self.rag.retrieve(query)
        if not context:
            context = "No relevant documents found."
        if isinstance(context, list):
            context = " ".join(context)
        response = self.llm.generate_response(
            context=context,
            query=query,
            role=role
        )
        return response