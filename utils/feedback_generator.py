# utils/feedback_generator.py

def generate_feedback(score_result):
    """
    Generate feedback based on the resume score and keyword match.
    
    Args:
        score_result (dict): Dictionary returned from score_resume function.
    
    Returns:
        str: Feedback message.
    """
    tips = []

    sim_score = score_result.get("cosine_similarity", 0)
    keyword_score = score_result.get("keyword_coverage", 0)

    if sim_score < 50:
        tips.append("Increase similarity by aligning your experience with the job description more closely.")
    elif sim_score < 75:
        tips.append("You’re doing well! Consider fine-tuning language to reflect the job description better.")
    else:
        tips.append("Great! Your resume is well-aligned with the job description.")

    if keyword_score < 40:
        tips.append("Add more relevant keywords from the job description to your resume.")
    elif keyword_score < 75:
        tips.append("You're on track! Try to include a few more job-specific keywords.")
    else:
        tips.append("Nice work! You've included most of the important keywords.")

    if not score_result.get("matched_keywords"):
        tips.append("Consider tailoring your resume with industry-specific terms.")

    return " ".join(tips)
