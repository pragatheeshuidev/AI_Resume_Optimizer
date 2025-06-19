# utils/file_utils.py

import os
import re

def is_filename_professional(filename):
    """
    Checks if the given filename looks professional (no emojis, no special chars, uses underscores/dashes, etc.)

    Args:
        filename (str): The filename string (without path).

    Returns:
        bool: True if filename looks professional, else False.
    """
    name, _ = os.path.splitext(filename)
    pattern = r'^[a-zA-Z0-9_\-]+$'
    return bool(re.match(pattern, name))


def clean_text(text):
    """
    Removes extra spaces, special characters, and lowercases the text.

    Args:
        text (str): Raw text input.

    Returns:
        str: Cleaned text.
    """
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^\w\s]', '', text)
    return text.lower().strip()
