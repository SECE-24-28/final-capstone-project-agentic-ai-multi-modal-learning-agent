from core.embeddings import EmbeddingEngine
from core.vector_store import VectorStore

class RAGPipeline:
    def __init__(self):
        self.embedder = EmbeddingEngine()
        self.vector_store = VectorStore()

    def add_document(self, text):
        if text and len(text.strip()) > 0:
            vector = self.embedder.embed_text(text)
            self.vector_store.add_vector(vector, text)

    def retrieve(self, query):
        query_vector = self.embedder.embed_text(query)
        docs = self.vector_store.search(query_vector)
        if not docs:
            return "No relevant documents found."
        return " ".join(docs)