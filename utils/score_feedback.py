import json
import os

score_data = {
    "candidate_name": "Pragatheesh K",
    "resume_score": 82,
    "grammar_score": 88,
    "linkedin_score": 75,
    "keyword_match_score": 90,
    "summary": "Good profile, but LinkedIn improvements recommended."
}

output_path = os.path.join("outputs", "resume_score.json")
with open(output_path, "w") as f:
    json.dump(score_data, f, indent=4)
