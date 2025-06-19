# AI Resume Optimizer 🚀

> Transform boring resumes into job-winning powerhouses using AI.

## 📌 Problem Statement

Candidates often struggle with resume shortlisting due to mismatches in skill alignment, poor formatting, and lack of keyword optimization. Recruiters also waste time on irrelevant resumes. We propose an AI-powered tool that semantically analyzes and scores resumes against job descriptions for better matches.

## 💡 Solution

This app extracts text from resumes, performs NLP-based skill matching with job descriptions, scores each resume, and provides optimization tips using AI (BERT + traditional ML).

## 🛠️ Features

- 📄 Upload multiple resumes (PDF/DOCX)
- 📝 Paste Job Description or Upload JD File
- 🤖 Semantic Resume Matching (using BERT embeddings)
- 📈 Resume Score + Skill Gap Analysis
- ✅ Keyword Highlighting & Grammar Check
- 🧠 Optimization Tips (Text Complexity + Suggestions)
- 📊 Dashboard: Top skills, average scores, keyword match, etc.
- 🧾 Export reports for each resume

## 🧰 Tech Stack

- **Python**, **Streamlit** for UI
- **Pandas**, **NumPy**, **Scikit-learn**
- **Sentence Transformers (BERT)** for semantic similarity
- **NLTK**, **Textstat** for grammar & readability
- **Matplotlib**, **Seaborn** for dashboard
- **PDFMiner**, **python-docx** for file handling



