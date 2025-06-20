# app.py
import streamlit as st
from utils.resume_parser import parse_resume
from utils.job_description_cleaner import clean_job_description
from utils.similarity import compute_similarity
from utils.resume_scorer import calculate_score
from utils.grammar_checker import check_grammar
from utils.feedback_generator import generate_feedback

st.set_page_config(page_title="AI Resume Optimizer", layout="wide")

st.title("📄 AI Resume Optimizer")

# Upload resumes
uploaded_files = st.file_uploader("Upload one or more resumes", type=["pdf", "docx"], accept_multiple_files=True)

# Paste or Upload Job Description
jd_text = st.text_area("Paste Job Description")
jd_file = st.file_uploader("Or upload JD file", type=["txt", "pdf", "docx"])

if jd_file:
    jd_text = jd_file.read().decode("utf-8")

if uploaded_files and jd_text:
    jd_clean = clean_job_description(jd_text)

    for file in uploaded_files:
        with st.spinner(f"Processing {file.name}..."):
            resume_text = parse_resume(file)
            similarity_score = compute_similarity(resume_text, jd_clean)
            score = calculate_score(resume_text, jd_clean)
            grammar_issues = check_grammar(resume_text)
            feedback = generate_feedback(resume_text, jd_clean)

            st.subheader(file.name)
            st.metric("Match %", f"{similarity_score:.2f}")
            st.metric("Resume Score", f"{score}/100")
            st.text("🔍 Feedback")
            st.write(feedback)

            with st.expander("🔧 Grammar Suggestions"):
                st.write(grammar_issues)

            st.markdown("---")
