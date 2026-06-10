import chromadb

client = chromadb.PersistentClient(
    path="D:/Multimodal_learning agent/early_edu_ai/data/chromadb"
)

collection = client.get_or_create_collection("edu_collection")

print(f"Total documents stored: {collection.count()}")

if collection.count() > 0:
    results = collection.get()
    print("\nStored documents:")
    for i, doc in enumerate(results['documents']):
        print(f"\n--- Document {i+1} ---")
        print(doc[:200])