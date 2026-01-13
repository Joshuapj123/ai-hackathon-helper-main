import streamlit as st
from project_generator import generate_project

st.set_page_config(page_title="AI Hackathon Helper", layout="centered")

st.title("🤖 AI Hackathon Helper")

prompt = st.text_area(
    "Describe your hackathon problem statement:",
    height=150
)

if st.button("Generate Project Idea"):
    if prompt.strip():
        result = generate_project(prompt)
        st.success("Project Generated Successfully!")
        st.text(result)
    else:
        st.warning("Please enter a problem statement.")

