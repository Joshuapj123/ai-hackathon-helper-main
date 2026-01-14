from ml_engine import generate_summary, extract_keywords, compute_similarity

def generate_project(problem_text, proposed_solution=""):
    # Extract keywords
    keywords = extract_keywords(problem_text)
    
    # Compute semantic similarity if proposed solution exists
    score = compute_similarity(problem_text, proposed_solution) if proposed_solution else 0.0
    
    # Generate project summary
    summary = generate_summary(problem_text, proposed_solution)
    
    # Core features
    features = [
        "Problem statement understanding using NLP",
        "Keyword extraction and domain identification",
        "Semantic similarity evaluation using ML",
        "Automated AI project idea generation",
        "Visualization and reporting of insights"
    ]
    
    # Technology stack
    tech_stack = [
        "Python",
        "Natural Language Processing (NLP)",
        "Machine Learning (TF-IDF, Cosine Similarity)",
        "Scikit-learn, Pandas, Numpy",
        "Streamlit for web interface"
    ]
    
    # Impact
    impact = "Helps quickly choose meaningful and practical hackathon projects, saving time and improving innovation quality."
    
    return {
        "summary": summary,
        "keywords": keywords,
        "score": score,
        "features": features,
        "tech_stack": tech_stack,
        "impact": impact
    }








