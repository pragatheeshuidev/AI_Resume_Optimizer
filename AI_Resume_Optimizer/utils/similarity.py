# utils/similarity.py

from sentence_transformers import SentenceTransformer, util

# Load the model once (you can cache this if needed)
model = SentenceTransformer('all-MiniLM-L6-v2')

def calculate_similarity(resume_text, job_description):
    embeddings = model.encode([resume_text, job_description], convert_to_tensor=True)
    score = util.cos_sim(embeddings[0], embeddings[1]).item()
    return round(score * 100, 2)  # Return score as percentage
