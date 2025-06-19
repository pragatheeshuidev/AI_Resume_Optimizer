import streamlit as st
import os

from utils.resume_parser import parse_resume
from utils.job_description_cleaner import clean_job_description
from utils.similarity import calculate_similarity
from utils.resume_scorer import score_resume
from utils.feedback_generator import generate_feedback, generate_overall_feedback
from utils.score_feedback import generate_score_feedback
from utils.grammar_check import check_grammar
from utils.linkedin_checker import check_linkedin
from utils.extract_text import extract_text_from_pdf

# --- Streamlit App Setup ---
st.set_page_config(page_title="AI Resume Optimizer", layout="wide")
st.title("🤖 AI Resume Optimizer & Matching Tool")
st.markdown("Upload your resume and job description to get instant feedback, score, and optimization tips!")

# --- File Uploads ---
resume_file = st.file_uploader("📄 Upload Your Resume (PDF only)", type=["pdf"])
job_description = st.text_area("📝 Paste the Job Description here")

if st.button("🔍 Analyze Resume"):

    if resume_file is None or not job_description.strip():
        st.warning("Please upload a resume and paste the job description to continue.")
        st.stop()

    with st.spinner("🔍 Extracting and analyzing your resume..."):

        # Extract and parse resume text
        resume_text = extract_text_from_pdf(resume_file)
        parsed_resume = parse_resume(resume_text)

        # Clean JD
        cleaned_jd = clean_job_description(job_description)

        # Resume Score
        resume_score = score_resume(parsed_resume)

        # Semantic Similarity
        similarity_score = calculate_similarity(resume_text, cleaned_jd)

        # Feedback
        feedback = generate_score_feedback(resume_score)
        overall_feedback = generate_overall_feedback(resume_score, similarity_score)

        # LinkedIn Check
        linkedin_score = check_linkedin(resume_text)

        # Grammar Check
        grammar_issues = check_grammar(resume_text)

    # --- Output Sections ---
    st.subheader("📊 Resume Score & Match Analysis")
    st.metric("Resume Score", f"{resume_score}/100")
    st.metric("Job Match Similarity", f"{similarity_score:.2f}/1.0")
    st.metric("LinkedIn Score", f"{linkedin_score}/10")

    st.subheader("🗣️ Overall Feedback")
    st.success(overall_feedback)

    st.subheader("✅ Optimization Suggestions")
    st.write(feedback)

    if grammar_issues:
        st.subheader("📝 Grammar Issues Found")
        for issue in grammar_issues:
            st.error(f"⚠️ {issue}")
    else:
        st.success("🎯 No major grammar issues found.")

    st.subheader("📌 Extracted Resume Sections")
    for key, value in parsed_resume.items():
        if value:
            st.markdown(f"**{key.capitalize()}**")
            st.write(value)

st.markdown("---")
st.caption("🔐 Your data is processed securely and never stored.")
