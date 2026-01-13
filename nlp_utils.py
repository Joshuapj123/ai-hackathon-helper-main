import nltk
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z ]', '', text)
    tokens = word_tokenize(text)
    tokens = [w for w in tokens if w not in stop_words]
    return " ".join(tokens)

#ml_engine.py
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def semantic_score(text1, text2):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([text1, text2])
    score = cosine_similarity(vectors[0], vectors[1])[0][0]
    return round(score * 100, 2)

def extract_keywords(text, top_n=7):
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform([text])
    scores = zip(vectorizer.get_feature_names_out(), X.toarray()[0])
    sorted_words = sorted(scores, key=lambda x: x[1], reverse=True)
    return [word for word, score in sorted_words[:top_n]]

#generator.py
from nlp_utils import clean_text
from ml_engine import semantic_score, extract_keywords

def generate_project(theme, idea, skills):
    clean_idea = clean_text(idea)
    clean_theme = clean_text(theme)

    alignment = semantic_score(clean_idea, clean_theme)
    keywords = extract_keywords(clean_idea)

    title = f"AI-Driven {keywords[0].title()} Assistant"

    problem = f"""
Hackathon participants often face difficulty converting raw ideas into structured,
high-quality project submissions within limited time. This leads to weak explanations,
poor presentations, and reduced evaluation scores.
"""

    solution = f"""
This project proposes an AI-powered hackathon productivity assistant that uses
Natural Language Processing and Machine Learning techniques to analyze ideas,
understand hackathon themes, and generate structured project content automatically.
"""

    features = [
        "NLP-based idea understanding",
        "Semantic alignment with hackathon themes",
        "ML-driven keyword extraction",
        "Automated project structuring",
        "Submission-ready documentation generation"
    ]

    tech_stack = ["Python", "Streamlit", "NLP", "TF-IDF", "Cosine Similarity"]

    submission = f"""
PROJECT TITLE:
{title}

THEME ALIGNMENT SCORE:
{alignment} %

KEY IDEA KEYWORDS:
{', '.join(keywords)}

PROBLEM STATEMENT:
{problem}

PROPOSED SOLUTION:
{solution}

KEY FEATURES:
- {'\n- '.join(features)}

TECH STACK:
- {', '.join(tech_stack)}
"""

    return {
        "title": title,
        "alignment": alignment,
        "keywords": keywords,
        "problem": problem,
        "solution": solution,
        "features": features,
        "tech_stack": tech_stack,
        "submission": submission
    }

#app.py
import streamlit as st
from generator import generate_project

st.set_page_config(page_title="AI Hackathon Helper", layout="centered")

st.title("🚀 AI Hackathon Helper")
st.caption("AI + NLP + ML powered productivity tool for hackathons")

theme = st.text_input("Hackathon Theme")
idea = st.text_area("Describe Your Idea")
skills = st.text_input("Your Skills (Python, ML, Web, etc.)")

if st.button("Generate AI Project"):
    if theme and idea and skills:
        result = generate_project(theme, idea, skills)

        st.success("AI Analysis Completed")

        st.metric("Theme Alignment Score", f"{result['alignment']} %")

        st.header("📌 Project Title")
        st.write(result["title"])

        st.header("🧠 Extracted Keywords")
        st.write(", ".join(result["keywords"]))

        st.header("❗ Problem Statement")
        st.write(result["problem"])

        st.header("💡 Solution Overview")
        st.write(result["solution"])

        st.header("✨ Features")
        for f in result["features"]:
            st.write("- ", f)

        st.header("🛠️ Technology Stack")
        for t in result["tech_stack"]:
            st.write("- ", t)

        st.header("📄 Submission Content")
        st.code(result["submission"])

    else:
        st.warning("Please fill all fields")
