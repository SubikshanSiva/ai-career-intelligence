from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


resume = input("Enter resume text:\n")

job_description = input("\nEnter target job description:\n")


documents = [
    resume,
    job_description
]

vectorizer = TfidfVectorizer(
    lowercase=True,
    stop_words="english"
)

features = vectorizer.fit_transform(documents)

similarity = cosine_similarity(
    features[0:1],
    features[1:2]
)[0][0]


print("\nFeature Matrix Shape:")
print(features.shape)

print("\nTF-IDF Features:")
print(vectorizer.get_feature_names_out())

print("\nResume-Job Similarity:")
print(round(similarity * 100, 2), "%")