# utils/score_feedback.py

def generate_score_feedback(score):
    """
    Generates feedback based on the resume score.
    """
    if score >= 90:
        return "Outstanding resume! You're job-market ready!"
    elif score >= 75:
        return "Great job! A few tweaks and you're there."
    elif score >= 60:
        return "Good effort! Add more keywords and details."
    elif score >= 40:
        return "Needs improvement. Focus on key skills and structure."
    else:
        return "Major update required. Start with format and essential sections."
