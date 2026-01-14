import streamlit as st
from bytez import Bytez

# --------------------
# CONFIG
# --------------------
API_KEY = "72537a96ed58d29910699530c8a21e78"
sdk = Bytez(API_KEY)
model = sdk.model("openai/gpt-5")  # GPT-5 model

# --------------------
# STREAMLIT UI
# --------------------
st.set_page_config(page_title="AI Hackathon Helper", layout="centered")
st.title("🤖 AI Hackathon Helper")
st.write("Analyze a hackathon problem statement and generate an AI-based project idea.")

problem = st.text_area("📌 Enter Problem Statement")
proposed = st.text_area("💡 Enter Proposed Solution (Optional – press Enter to skip)")

# --------------------
# BUTTON
# --------------------
if st.button("🚀 Generate Project Idea"):

    if not problem.strip():
        st.error("Please enter a problem statement.")
    else:
        # Construct prompt dynamically
        prompt = f"""
Analyze the following hackathon problem statement and generate an AI-powered project idea.
Return output in this format:

Project Summary:
Keywords (list):
Core Features (list):
Technology Stack (list):
Impact:

Problem Statement: {problem}
Proposed Solution: {proposed if proposed.strip() != '' else 'None'}
"""

        # Show spinner while waiting for API
        with st.spinner("Generating AI project idea..."):
            try:
                response = model.run([
                    {"role": "user", "content": prompt}
                ])

                # Bytez API returns output as a dict
                if response.output and response.output.get("content"):
                    output_text = response.output["content"]

                    st.markdown("## 🚀 Project Output")
                    st.text(output_text)

                else:
                    st.error("🚫 AI returned no output. Try again or rephrase the problem.")

            except Exception as e:
                st.error(f"⚠️ Error calling Bytez API: {e}")





















