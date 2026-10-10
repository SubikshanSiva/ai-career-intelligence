
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

resume = input("Enter your resume text:\n")

jobs = [
    {
        "title": "Python Backend Developer",
        "description": "Develop backend applications using Python, APIs, SQL and databases."
    },
    {
        "title": "AI Engineer",
        "description": "Build machine learning models using Python, NLP, deep learning and embeddings."
    },
    {
        "title": "Frontend Developer",
        "description": "Build responsive user interfaces using HTML, CSS, JavaScript and React."
    },
    {
        "title": "Data Analyst",
        "description": "Analyze datasets using SQL, Python, Excel and data visualization."
    }
]

job_descriptions = [job["description"] for job in jobs]

resume_embedding = model.encode(
    resume,
    convert_to_tensor=True
)

job_embeddings = model.encode(
    job_descriptions,
    convert_to_tensor=True
)

similarities = util.cos_sim(
    resume_embedding,
    job_embeddings
)[0]

ranked_jobs = sorted(
    zip(jobs, similarities.tolist()),
    key=lambda item: item[1],
    reverse=True
)

print("\nRanked Job Recommendations:")

for rank, (job, score) in enumerate(ranked_jobs, start=1):
    print(f"\n{rank}. {job['title']}")
    print(f"   Similarity Score: {score:.4f}")
    print(f"   Description: {job['description']}")
