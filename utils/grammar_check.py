# utils/grammar_check.py

from textblob import TextBlob

def correct_grammar(text):
    """
    Takes a string input and returns the corrected text
    using basic grammar and spelling correction.
    """
    blob = TextBlob(text)
    return str(blob.correct())
