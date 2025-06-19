# utils/job_description_cleaner.py

import re
import string

def clean_jd_text(text):
    """
    Cleans job description text: lowercases, removes punctuation, numbers, emails, URLs, and extra spaces.
    """
    # Lowercase
    text = text.lower()

    # Remove email addresses
    text = re.sub(r'\S+@\S+', '', text)

    # Remove URLs
    text = re.sub(r'http\S+|www\S+', '', text)

    # Remove numbers
    text = re.sub(r'\d+', '', text)

    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()

    return text
