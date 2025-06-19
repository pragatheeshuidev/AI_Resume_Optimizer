# utils/resume_parser.py

import PyPDF2
import os

def extract_text_from_pdf(pdf_path):
    """
    Extracts and returns the raw text from a PDF resume.
    """
    text = ""
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                text += page.extract_text()
    except Exception as e:
        text = f"Error reading PDF: {e}"
    return text
