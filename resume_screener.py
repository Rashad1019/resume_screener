"""
AI Resume Screener with Python & Gemini API
Based on Aman Kharwal's tutorial, adapted to use Google's Gemini API
"""

import google.generativeai as genai
import fitz  # PyMuPDF
import json
import os
from datetime import datetime
from glob import glob

# Configure Gemini - Set your API key here or use environment variable
# Get your API key from: https://aistudio.google.com/app/apikey
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "your-gemini-api-key")
genai.configure(api_key=GEMINI_API_KEY)

# Initialize the Gemini model
model = genai.GenerativeModel('gemini-3-flash-preview')


# ============================================================
# STEP 1: THE READER
# LLMs can't see PDF files directly; they need raw text.
# We use PyMuPDF to extract text from PDF documents.
# ============================================================
def extract_text_from_pdf(pdf_path):
    """
    Extract text from a PDF file.
    
    Args:
        pdf_path: Path to the PDF file
        
    Returns:
        Extracted text as a string
    """
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    doc.close()
    return text


# ============================================================
# STEP 2: THE BRAIN
# This is the key part - we use prompt engineering to give
# the AI a persona (Senior Technical Recruiter) and specific
# constraints (JSON format output).
# ============================================================
def screen_resume(resume_text, job_description):
    """
    Screen a resume against a job description using Gemini AI.
    
    Args:
        resume_text: The extracted text from the resume PDF
        job_description: The job description to match against
        
    Returns:
        JSON string containing the screening results
    """
    prompt = f"""
    You are a Senior Technical Recruiter with 20 years of experience.
    Your goal is to objectively evaluate a candidate's resume against a job description.
    
    JOB DESCRIPTION:
    {job_description}
    
    CANDIDATE RESUME:
    {resume_text}
    
    TASK:
    Analyze the resume against the JD. Look for both exact and semantic matches.
    Be strict but fair. "React" matches "React.js", "ML" matches "Machine Learning".
    
    OUTPUT FORMAT:
    Provide the response in valid JSON format only with the following structure:
    {{
        "candidate_name": "extracted name",
        "match_score": "0-100",
        "key_strengths": ["list of 3 key strengths relevant to the JD"],
        "missing_critical_skills": ["list of missing skills required in JD"],
        "recommendation": "INTERVIEW" or "REJECT",
        "reasoning": "A 2-sentence summary of why this decision was made"
    }}
    
    Return ONLY the JSON object, no additional text or markdown formatting.
    """
    
    response = model.generate_content(prompt)
    return response.text


# ============================================================
# JOB DESCRIPTIONS
# Add or modify job descriptions here
# ============================================================
JOB_DESCRIPTIONS = {
    "1": {
        "title": "Junior Data Scientist",
        "description": """
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
    },
    "2": {
        "title": "Software Engineer",
        "description": """
        We are looking for a Software Engineer.
        Must have:
        - Proficiency in Python, Java, or JavaScript
        - Experience with web frameworks (Django, Flask, React, or Node.js)
        - Understanding of RESTful APIs and microservices
        - Version control with Git
        - Database experience (SQL and NoSQL)
        Nice to have:
        - Cloud experience (AWS, GCP, or Azure)
        - CI/CD pipeline experience
        - Docker and Kubernetes
        """
    },
    "3": {
        "title": "Data Analyst",
        "description": """
        We are looking for a Data Analyst.
        Must have:
        - Strong SQL skills
        - Experience with Excel and data visualization tools (Tableau, Power BI)
        - Python or R for data analysis
        - Ability to create reports and dashboards
        - Strong analytical and problem-solving skills
        Nice to have:
        - Experience with statistical analysis
        - Knowledge of ETL processes
        """
    },
    "4": {
        "title": "Fintech Operations Specialist",
        "description": """
        We are looking for a Fintech Operations Specialist.
        Must have:
        - Experience in financial services or fintech
        - Strong SQL skills for transaction analysis
        - Understanding of payment processing and compliance
        - Experience with fraud detection or risk analysis
        - Excellent communication and problem-solving skills
        Nice to have:
        - Experience with automation tools
        - Knowledge of regulatory requirements (AML, KYC)
        - Experience with data validation and quality assurance
        """
    },
    "5": {
        "title": "Product Manager",
        "description": """
        We are looking for a Product Manager.
        Must have:
        - Experience defining product roadmaps and requirements
        - Strong analytical skills and data-driven decision making
        - Excellent communication with stakeholders
        - Experience with Agile/Scrum methodology
        - Ability to prioritize features and manage backlogs
        Nice to have:
        - Technical background or understanding
        - Experience with user research and UX
        - SQL or data analysis skills
        """
    },
    "6": {
        "title": "Customer Success Manager",
        "description": """
        We are looking for a Customer Success Manager.
        Must have:
        - Experience in customer-facing roles
        - Strong communication and relationship-building skills
        - Ability to understand customer needs and provide solutions
        - Experience with CRM tools (Salesforce, HubSpot)
        - Track record of improving customer satisfaction
        Nice to have:
        - Technical product knowledge
        - Experience with data analysis for customer insights
        - Upselling and cross-selling experience
        """
    }
}


def generate_job_description(role_title):
    """Use AI to generate a job description based on a role title."""
    prompt = f"""
    Generate a professional job description for the role: {role_title}
    
    Format:
    We are looking for a {role_title}.
    Must have:
    - [5-7 key requirements]
    Nice to have:
    - [2-3 preferred skills]
    
    Keep it concise and realistic. Return ONLY the job description text.
    """
    
    response = model.generate_content(prompt)
    return response.text


def get_job_description():
    """Display menu and get job description from user."""
    print("\n" + "="*50)
    print("         SELECT JOB ROLE")
    print("="*50)
    
    for key, job in JOB_DESCRIPTIONS.items():
        print(f"  [{key}] {job['title']}")
    print(f"  [7] Custom (enter role or description)")
    print("="*50)
    
    choice = input("\nEnter your choice (1-7): ").strip()
    
    if choice in JOB_DESCRIPTIONS:
        print(f"\n[OK] Selected: {JOB_DESCRIPTIONS[choice]['title']}")
        return JOB_DESCRIPTIONS[choice]['description']
    elif choice == "7":
        print("\n" + "-"*50)
        print("CUSTOM JOB OPTIONS:")
        print("  [A] Enter a role title (AI will generate JD)")
        print("  [B] Enter full job description manually")
        print("-"*50)
        
        sub_choice = input("\nEnter A or B: ").strip().upper()
        
        if sub_choice == "A":
            role_title = input("\nEnter the role title (e.g., 'Backend Developer'): ").strip()
            if role_title:
                print(f"\n[AI] Generating job description for '{role_title}'...")
                return generate_job_description(role_title)
            else:
                print("[WARNING] No role entered. Using default.")
                return JOB_DESCRIPTIONS["1"]["description"]
        else:
            print("\nEnter your job description (press Enter twice when done):")
            lines = []
            while True:
                line = input()
                if line == "":
                    break
                lines.append(line)
            return "\n".join(lines)
    else:
        print("[WARNING] Invalid choice. Using default: Junior Data Scientist")
        return JOB_DESCRIPTIONS["1"]["description"]


# ============================================================
# STEP 3: PROCESS A SINGLE RESUME
# ============================================================
def process_single_resume(resume_path, job_description):
    """Process a single resume and return the result data."""
    try:
        resume_text = extract_text_from_pdf(resume_path)
        print(f"[OK] Resume loaded. Length: {len(resume_text)} characters.")
    except Exception as e:
        print(f"[ERROR] Error loading resume: {e}")
        return None
    
    print("[AI] Analyzing the candidate... (this may take a few seconds)")
    
    try:
        result_json_string = screen_resume(resume_text, job_description)
    except Exception as e:
        print(f"[ERROR] Error during AI screening: {e}")
        return None
    
    try:
        clean_json = result_json_string.replace("```json", "").replace("```", "").strip()
        result_data = json.loads(clean_json)
        return result_data
    except json.JSONDecodeError:
        print("[WARNING] Failed to parse JSON. Raw output:")
        print(result_json_string)
        return None


def generate_report(result_data):
    """Generate a formatted report from result data."""
    report_lines = []
    report_lines.append("=" * 50)
    report_lines.append("         SCREENING REPORT")
    report_lines.append("=" * 50)
    report_lines.append(f"\nCandidate: {result_data.get('candidate_name', 'Unknown')}")
    report_lines.append(f"Match Score: {result_data.get('match_score', 'N/A')}/100")
    report_lines.append(f"Decision: {result_data.get('recommendation', 'N/A')}")
    
    report_lines.append(f"\nKey Strengths:")
    for strength in result_data.get('key_strengths', []):
        report_lines.append(f"   - {strength}")
    
    report_lines.append(f"\nMissing Skills:")
    missing_skills = result_data.get('missing_critical_skills', [])
    if missing_skills:
        for skill in missing_skills:
            report_lines.append(f"   - {skill}")
    else:
        report_lines.append("   - None identified")
    
    report_lines.append(f"\nReasoning: {result_data.get('reasoning', 'N/A')}")
    report_lines.append("\n" + "=" * 50)
    
    return "\n".join(report_lines)


def save_result(result_data, results_folder="results"):
    """Save the result to a file with unique name."""
    # Create results folder if it doesn't exist
    if not os.path.exists(results_folder):
        os.makedirs(results_folder)
    
    # Generate unique filename
    candidate_name = result_data.get('candidate_name', 'Unknown')
    safe_name = "".join(c if c.isalnum() or c in (' ', '-', '_') else '_' for c in candidate_name)
    safe_name = safe_name.replace(' ', '_')
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{safe_name}_{timestamp}.txt"
    filepath = os.path.join(results_folder, filename)
    
    # Generate and save report
    report_text = generate_report(result_data)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(report_text)
    
    return filepath


# ============================================================
# STEP 4: MAIN EXECUTION WITH MODE SELECTION
# ============================================================
def main():
    print("\n" + "=" * 50)
    print("      AI RESUME SCREENER")
    print("=" * 50)
    print("\nSelect mode:")
    print("  [1] Screen single resume")
    print("  [2] Screen batch (folder of resumes)")
    print("=" * 50)
    
    mode = input("\nEnter your choice (1 or 2): ").strip()
    
    # Get job description first (applies to both modes)
    job_description = get_job_description()
    
    if mode == "1":
        # Single resume mode
        resume_path = input("\nEnter the path to the resume PDF: ").strip()
        resume_path = resume_path.strip('"').strip("'").strip().lstrip('\ufeff')
        
        if not resume_path:
            print("No path provided. Using sample resume path.")
            resume_path = "sample_resume.pdf"
        
        print(f"\nProcessing: {os.path.basename(resume_path)}")
        result_data = process_single_resume(resume_path, job_description)
        
        if result_data:
            report = generate_report(result_data)
            print("\n" + report)
            
            filepath = save_result(result_data)
            print(f"\n[SAVED] Results saved to: {filepath}")
    
    elif mode == "2":
        # Batch mode
        folder_path = input("\nEnter the path to the folder containing resumes: ").strip()
        folder_path = folder_path.strip('"').strip("'").strip().lstrip('\ufeff')
        
        if not os.path.isdir(folder_path):
            print(f"[ERROR] Folder not found: {folder_path}")
            return
        
        # Find all PDF files in the folder
        pdf_files = glob(os.path.join(folder_path, "*.pdf")) + glob(os.path.join(folder_path, "*.PDF"))
        
        if not pdf_files:
            print(f"[ERROR] No PDF files found in: {folder_path}")
            return
        
        print(f"\n[OK] Found {len(pdf_files)} resume(s) to process.")
        print("-" * 50)
        
        results_summary = []
        
        for i, pdf_path in enumerate(pdf_files, 1):
            print(f"\n[{i}/{len(pdf_files)}] Processing: {os.path.basename(pdf_path)}")
            result_data = process_single_resume(pdf_path, job_description)
            
            if result_data:
                filepath = save_result(result_data)
                candidate = result_data.get('candidate_name', 'Unknown')
                score = result_data.get('match_score', 'N/A')
                decision = result_data.get('recommendation', 'N/A')
                results_summary.append({
                    'name': candidate,
                    'score': score,
                    'decision': decision,
                    'file': filepath
                })
                print(f"    -> {candidate}: {score}/100 - {decision}")
                print(f"    -> Saved to: {filepath}")
        
        # Print summary
        print("\n" + "=" * 50)
        print("         BATCH SUMMARY")
        print("=" * 50)
        print(f"\nProcessed: {len(results_summary)}/{len(pdf_files)} resumes\n")
        
        # Sort by score (highest first)
        try:
            results_summary.sort(key=lambda x: int(x['score']), reverse=True)
        except:
            pass
        
        print(f"{'Candidate':<25} {'Score':<10} {'Decision':<12}")
        print("-" * 50)
        for r in results_summary:
            print(f"{r['name']:<25} {r['score']:<10} {r['decision']:<12}")
        
        print("\n" + "=" * 50)
        print(f"Results saved to: results/ folder")
        print("=" * 50)
    
    else:
        print("[WARNING] Invalid choice. Please run again and select 1 or 2.")


if __name__ == "__main__":
    main()
