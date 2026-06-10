import chromadb
import uuid


class VectorStore:
    def __init__(self):
        self.client = chromadb.PersistentClient(
            path="D:/Multimodal_learning agent/early_edu_ai/data/chromadb"
        )
        self.collection = self.client.get_or_create_collection(
            name="edu_collection",
            metadata={"hnsw:space": "cosine"}
        )
        print("ChromaDB connected locally!")

    def add_vector(self, vector, text):
        try:
            existing = self.collection.get(include=["documents"])
            documents = existing.get("documents", []) if isinstance(existing, dict) else []

            if text in documents:
                print("Document already exists, skipping!")
                return

            embedding = vector.tolist() if hasattr(vector, "tolist") else list(vector)

            self.collection.add(
                embeddings=[embedding],
                documents=[text],
                ids=[str(uuid.uuid4())]
            )
            print(f"Document stored! Total: {self.collection.count()}")
        except Exception as exc:
            print(f"Add error: {exc}")
            raise

    def search(self, query_vector, top_k=3):
        try:
            count = self.collection.count()
            if count == 0:
                return []

            embedding = query_vector.tolist() if hasattr(query_vector, "tolist") else list(query_vector)

            results = self.collection.query(
                query_embeddings=[embedding],
                n_results=min(top_k, count)
            )

            documents = results.get("documents", [[]])[0]
            return documents if documents else []
        except Exception as e:
            print(f"Search error: {e}")
            return []

    def clear(self):
        self.client.delete_collection("edu_collection")
        self.collection = self.client.get_or_create_collection(
            name="edu_collection",
            metadata={"hnsw:space": "cosine"}
        )