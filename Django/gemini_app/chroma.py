# services/chroma.py
import chromadb
from chromadb.config import Settings

client = chromadb.HttpClient(host='localhost', port=8001)
# client = chromadb.Client(Settings(chroma_db_impl="duckdb+parquet", persist_directory=".chroma"))
collection = client.get_or_create_collection("my_collection")

def add_to_chroma(documents, ids, metadatas=None, embeddings=None):
    print("Adding to Chroma:")
    print(f"  Documents: {documents}")
    print(f"  IDs: {ids}")
    print(f"  Metadatas: {metadatas}")
    # print(f"  Embeddings: {embeddings}") # Don't print large embeddings
    collection.add(
        documents=documents,
        ids=ids,
        metadatas=metadatas,
        embeddings=embeddings  # Optional if using built-in embedding function
    )
    print("Successfully added to Chroma!")

# def add_to_chroma(documents, ids, metadatas=None, embeddings=None):
#     collection.add(
#         documents=documents,
#         ids=ids,
#         metadatas=metadatas,
#         embeddings=embeddings  # Optional if using built-in embedding function
#     )

def query_chroma(query_texts, n_results=3):
    return collection.query(query_texts=query_texts, n_results=n_results)
