# utils/linkedin_checker.py

import re

def has_linkedin_link(text):
    """
    Check if the resume text contains a valid LinkedIn URL.
    Returns True if found, otherwise False.
    """
    pattern = r"(https?://)?(www\.)?linkedin\.com/in/[A-Za-z0-9\-_/]+"
    return bool(re.search(pattern, text))
