import google.generativeai as genai
import fitz  # PyMuPDF
import json

# Configure Gemini
genai.configure(api_key="AIzaSyBsPk0PNrdfnhWrddIhV9ORYQifi3UEODs")

model = genai.GenerativeModel('gemini-3-flash-preview')  # ← Only this line changed!

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def screen_resume(resume_text, job_description):
    prompt = f"""You are a Senior Technical Recruiter with 20 years... [same full prompt as in the article]"""
    response = model.generate_content(prompt)
    return response.text  # Gemini returns text directly

# Rest of the code remains almost identical