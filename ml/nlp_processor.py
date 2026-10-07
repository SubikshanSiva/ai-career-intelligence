import nltk
import re

nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("stopwords")

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


def clean_text(text):
    text = text.lower()

    text = re.sub(r"[^a-zA-Z\s]", "", text)

    words = word_tokenize(text)

    stop_words = set(stopwords.words("english"))

    words = [
        word for word in words
        if word not in stop_words
    ]

    return words


resume = input("Enter resume text:\n")

processed_text = clean_text(resume)

print("\nProcessed Resume:")
print(processed_text)