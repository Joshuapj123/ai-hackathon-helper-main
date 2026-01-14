import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def simple_tokenize(text):
    """Simple tokenizer using regex (avoids NLTK punkt issues)"""
    tokens = re.findall(r'\b\w+\b', text.lower())
    return tokens

def extract_keywords(text, top_n=12):
    """Extract top N keywords using TF-IDF"""
    tokens = simple_tokenize(text)
    if not tokens:
        return []
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([" ".join(tokens)])
    scores = dict(zip(vectorizer.get_feature_names_out(), tfidf_matrix.toarray()[0]))
    sorted_keywords = sorted(scores, key=scores.get, reverse=True)[:top_n]
    return sorted_keywords

def compute_semantic_score(text1, text2):
    """Compute cosine similarity between problem and proposed solution"""
    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform([text1, text2])
    score = cosine_similarity(tfidf[0:1], tfidf[1:2])[0][0]
    return score

def generate_summary(problem, proposed_solution=""):
    """Generate a concise project summary"""
    if proposed_solution.strip() == "":
        return f"An AI-powered system to address the following problem:\n{problem}"
    else:
        return f"An AI-powered system designed to solve:\n{problem}\nUsing the proposed solution:\n{proposed_solution}"













