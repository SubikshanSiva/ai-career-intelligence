
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")

resume = input("Enter resume text:\n")
job_description = input("\nEnter job description:\n")

texts = [resume, job_description]

embeddings = model.encode(texts)

similarity = cosine_similarity(
    [embeddings[0]],
    [embeddings[1]]
)[0][0]

score = max(0, min(100, similarity * 100))

print("\nEmbedding Model: all-MiniLM-L6-v2")
print("Resume Embedding Shape:", embeddings[0].shape)
print("Job Embedding Shape:", embeddings[1].shape)
print("Semantic Similarity:", round(score, 2), "%")