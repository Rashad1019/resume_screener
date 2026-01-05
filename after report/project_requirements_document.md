# 🧱 Universal PRD (Project Requirements Document)

> ✅ Standardized workflow for data science, dashboard, and analytical projects  
> ✅ One-task-at-a-time execution with subtasks  
> ✅ Designed for both technical and non-technical audiences

---

## 📋 Project: AI Resume Screener (Llama 3 Local Edition)

**Author:** Rashad Ferguson  
**Email:** Rashad19@outlook.com  
**GitHub:** https://github.com/Rashad1019/resume_screener

---

## 2. 📝 README.md — ✅ Complete  
**Goal:** Serve as the public-facing project introduction.

**File:** [README.md](README.md)

**Included:**
- ✅ Project overview (AI-powered screening using Ollama/Llama 3)
- ✅ Key Features:
    - **Batch Processing:** Screen entire folders of resumes at once.
    - **Flexible Job Descriptions:** Use presets or generate custom JDs on the fly.
    - **Structured Output:** Results saved as standardized text reports.
- ✅ Setup instructions (API Key configuration)
- ✅ Usage guide (Menu system: Single vs Batch, Custom JDs)
- ✅ Credits to Aman Kharwal for the original concept

---

## 3. 🧠 Summary Document — ✅ Complete  
**Goal:** Explain the project clearly to non-technical readers.

**File:** [summary_report.md](summary_report.md)

**Included:**
- ✅ The Problem: Manual resume screening is slow and biased.
- ✅ The Solution: AI-assisted matching against specific job criteria.
- ✅ Workflow: How the tool ingests PDFs and outputs "Match/No Match" decisions.
- ✅ Value Add: Time-saving metrics and standardized evaluation.

---

## 4. 🛠️ Technical Implementation — ✅ Complete  
**Goal:** Provide details on how the project works technically.

**File:** [../resume_screener.py](../resume_screener.py) (Main Application)

**Technical Details:**
- **Core Engine:** Meta Llama 3 (via `ollama`) for semantic analysis.
- **PDF Processing:** `PyMuPDF` for fast and accurate text extraction.
- **Architecture:** 
    - `extract_text_from_pdf`: Ingestion layer.
    - `screen_resume`: Logic layer (Prompt Engineering).
    - `main` / `batch_process`: Execution layer with menu system.
- **Security:** API keys managed via environment variables.

---

## 5. 📣 Promotion Post — ✅ Complete  
**Goal:** Promote the project on LinkedIn, Twitter, blog, etc.

**File:** [promotion_post.md](promotion_post.md)

**Included:**
- ✅ Post for Technical Network (Python/AI focus)
- ✅ Post for Recruiter/HR Network (Efficiency focus)
- ✅ Key features highlighted (Batch mode, Custom Roles)
- ✅ Hashtags: #AI #Python #Llama3 #RecruitmentTech

---

## 🎉 All Requirements Complete!

---
