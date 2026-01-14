from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re

# Stopwords to clean keywords
STOPWORDS = {"and", "for", "in", "the", "with", "a", "an", "of", "to", "on", "by"}

def clean_text(text):
    # Lowercase, remove non-alphanum chars
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", "", text)
    return text

def extract_keywords(text, top_n=12):
    text = clean_text(text)
    words = text.split()
    # Remove stopwords
    keywords = [w for w in words if w not in STOPWORDS]
    # Keep unique and top_n
    seen = set()
    keywords = [w for w in keywords if not (w in seen or seen.add(w))]
    return keywords[:top_n]

def compute_similarity(problem, proposed):
    if not proposed.strip():
        return 0.0
    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform([problem, proposed])
    score = cosine_similarity(tfidf[0:1], tfidf[1:2])[0][0]
    return score

def generate_summary(problem, proposed=""):
    if proposed.strip():
        summary = f"An AI-powered system designed to solve: {problem} Using the proposed solution: {proposed}"
    else:
        summary = f"An AI-powered system designed to solve: {problem}"
    return summary



