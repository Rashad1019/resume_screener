"""Test the AI Resume Screener with sample_resume.pdf"""

from resume_screener import extract_text_from_pdf, screen_resume
import json

# Job Description
job_description = """
We are looking for a Junior Data Scientist.
Must have:
- Python (Pandas, NumPy, Scikit-Learn)
- Experience with SQL
- Basic understanding of Machine Learning algorithms
- Good communication skills
Nice to have:
- Experience with AWS or Cloud deployment
- Knowledge of NLP
"""

# Load and screen the resume
print("Loading sample_resume.pdf...")
resume_text = extract_text_from_pdf("sample_resume.pdf")
print(f"[OK] Resume loaded. Length: {len(resume_text)} characters.\n")

print("[AI] Analyzing the candidate...")
result_json_string = screen_resume(resume_text, job_description)

# Parse and display
try:
    clean_json = result_json_string.replace("```json", "").replace("```", "").strip()
    result_data = json.loads(clean_json)
    
    print("\n" + "="*50)
    print("         SCREENING REPORT")
    print("="*50)
    print(f"\nCandidate: {result_data.get('candidate_name', 'Unknown')}")
    print(f"Match Score: {result_data.get('match_score', 'N/A')}/100")
    print(f"Decision: {result_data.get('recommendation', 'N/A')}")
    
    print(f"\nKey Strengths:")
    for strength in result_data.get('key_strengths', []):
        print(f"   - {strength}")
    
    print(f"\nMissing Skills:")
    missing_skills = result_data.get('missing_critical_skills', [])
    if missing_skills:
        for skill in missing_skills:
            print(f"   - {skill}")
    else:
        print("   - None identified")
    
    print(f"\nReasoning: {result_data.get('reasoning', 'N/A')}")
    print("\n" + "="*50)
    
except json.JSONDecodeError:
    print("\n⚠️  Failed to parse JSON. Raw output:")
    print(result_json_string)
