# utils/resume_scorer.py

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def score_resume(resume_text, job_desc, keywords=None):
    """
    Scores a resume based on similarity with the job description and keyword coverage.
    
    Args:
        resume_text (str): Text extracted from the resume.
        job_desc (str): Text of the job description.
        keywords (list): Optional list of important keywords to match.
    
    Returns:
        dict: Score breakdown including similarity, keyword match, and overall score.
    """
    # Cosine Similarity Score
    vectorizer = CountVectorizer().fit_transform([resume_text, job_desc])
    vectors = vectorizer.toarray()
    cosine_sim = cosine_similarity([vectors[0]], [vectors[1]])[0][0]

    # Keyword Match Score
    keyword_score = 0
    matched_keywords = []
    if keywords:
        resume_lower = resume_text.lower()
        for word in keywords:
            if word.lower() in resume_lower:
                keyword_score += 1
                matched_keywords.append(word)

        keyword_score_pct = keyword_score / len(keywords) if keywords else 0
    else:
        keyword_score_pct = 0

    # Final Weighted Score
    final_score = round((cosine_sim * 0.6 + keyword_score_pct * 0.4) * 100, 2)

    return {
        "cosine_similarity": round(cosine_sim * 100, 2),
        "keyword_coverage": round(keyword_score_pct * 100, 2),
        "matched_keywords": matched_keywords,
        "final_score": final_score
    }
