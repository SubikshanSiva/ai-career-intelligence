import nltk
import re

nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("stopwords")

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


def clean_text(text):

    text = text.lower()

    cleaned_text = re.sub(r"[^a-zA-Z\s]", "", text)

    words = word_tokenize(cleaned_text)

    stop_words = set(stopwords.words("english"))

    filtered_words = [
        word for word in words
        if word not in stop_words
    ]

    return filtered_words


resume = input("Enter resume text:\n")

processed_text = clean_text(resume)

print("\nOriginal Resume:")
print(resume)

print("\nProcessed Tokens:")
print(processed_text)

print("\nTotal Tokens:", len(processed_text))