
import chromadb
from chromadb.utils.embedding_functions import (
    SentenceTransformerEmbeddingFunction
)

embedding_function = SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(
    name="career_jobs",
    embedding_function=embedding_function
)

jobs = [
    {
        "id": "job1",
        "title": "Python Backend Developer",
        "description": "Develop backend applications using Python, APIs, SQL and databases."
    },
    {
        "id": "job2",
        "title": "AI Engineer",
        "description": "Build machine learning models using Python, NLP, deep learning and embeddings."
    },
    {
        "id": "job3",
        "title": "Frontend Developer",
        "description": "Build responsive interfaces using HTML, CSS, JavaScript and React."
    },
    {
        "id": "job4",
        "title": "Data Analyst",
        "description": "Analyze datasets using SQL, Python, Excel and data visualization."
    }
]

collection.upsert(
    ids=[job["id"] for job in jobs],
    documents=[job["description"] for job in jobs],
    metadatas=[
        {"title": job["title"]}
        for job in jobs
    ]
)

resume = input("Enter your resume text:\n")

results = collection.query(
    query_texts=[resume],
    n_results=min(3, collection.count())
)

print("\nTop Matching Jobs from ChromaDB:")

for i, job_id in enumerate(results["ids"][0]):
    title = results["metadatas"][0][i]["title"]
    description = results["documents"][0][i]
    distance = results["distances"][0][i]

    print(f"\n{i + 1}. {title}")
    print(f"   Distance: {distance:.4f}")
    print(f"   Description: {description}")
