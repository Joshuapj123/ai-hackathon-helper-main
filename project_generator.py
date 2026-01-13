import re
from collections import Counter

STOPWORDS = {
    "the", "is", "and", "to", "of", "a", "in", "for", "that",
    "with", "as", "are", "on", "this", "it", "an", "be"
}

def extract_keywords(text):
    text = text.lower()
    words = re.findall(r"[a-z]+", text)
    keywords = [w for w in words if w not in STOPWORDS and len(w) > 3]
    return Counter(keywords).most_common(6)

def generate_project(prompt):
    keywords = extract_keywords(prompt)
    keyword_list = ", ".join([k for k, _ in keywords])

    return f"""
🚀 AI Hackathon Project Proposal

🔹 Problem Summary:
Students face difficulty selecting meaningful hackathon projects due to time limits,
lack of AI knowledge, and unclear problem understanding.

🔹 Key Focus Areas:
{keyword_list}

🔹 Proposed AI Solution:
Develop an AI-powered assistant that uses Natural Language Processing (NLP)
to analyze problem statements, extract key requirements, and recommend
feasible and innovative AI-based project ideas.

🔹 Core Features:
• Problem statement analysis using NLP  
• Keyword extraction and domain detection  
• Project idea generation  
• Suggested technology stack  

🔹 Technology Stack:
• Python  
• NLP (Text preprocessing, keyword extraction)  
• Machine Learning (Scikit-learn – TF-IDF extension ready)  
• Streamlit (Web Interface)

🔹 Impact:
Helps students save time, choose better projects, and focus on implementation
rather than ideation.
"""

