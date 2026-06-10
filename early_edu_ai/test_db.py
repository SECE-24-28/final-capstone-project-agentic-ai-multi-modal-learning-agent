from core.rag_pipeline import RAGPipeline

# Initialize
rag = RAGPipeline()

# Add test document
rag.add_document("Math worksheet page 10. English reading chapter 3. Parent teacher meeting on Friday 3PM.")

# Check count
import chromadb
client = chromadb.PersistentClient(
    path="D:/Multimodal_learning agent/early_edu_ai/data/chromadb"
)
collection = client.get_or_create_collection("edu_collection")
print(f"Documents stored: {collection.count()}")

# Retrieve
result = rag.retrieve("what is the homework")
print(f"Retrieved: {result}")