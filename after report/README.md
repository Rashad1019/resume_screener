# AI Resume Screener with Python & Gemini

An AI-powered resume screening tool built with Python and Google's Gemini API. This tool helps recruiters and hiring managers quickly evaluate resumes against job descriptions using advanced AI analysis.

> **Note:** This project is based on the tutorial **"Build an AI Resume Screener with Python & Llama 3"** by **Aman Kharwal**, adapted to use **Google's Gemini API** for cloud-based inference and enhanced with batch processing capabilities.

---

## ✨ New Features (Added to Original Tutorial)

We enhanced the original project with these production-ready capabilities:

- **1. 📂 Batch Processing:** 
  - Screen an entire folder of PDF resumes in one go.
  - Automatically iterates through all files and generates a summary report.

- **2. 📝 Flexible Job Descriptions:** 
  - **Presets:** Choose from 6 common roles (Data Scientist, Software Engineer, etc.)
  - **Auto-Generate:** Enter a simple title (e.g., "React Developer") and the AI creates the JD.
  - **Custom Input:** Paste your specific job description text.

- **3. 🤖 Google Gemini Integration:** 
  - Replaced local Llama 3 with **Gemini 1.5 Flash** for faster, cloud-based inference.
  - No need to install Ollama or download heavy models.

- **4. 💾 Auto-Save & Structured Reporting:**
  - Every session saves a detailed text report to the `results/` folder.
  - Reports include Match Score, Decision, Strengths, Missing Skills, and Reasoning.

---

## 🚀 Setup

1. **Install Dependencies:**
   ```bash
   pip install google-generativeai pymupdf
   ```

2. **Configure API Key:**
   Get your API key from [Google AI Studio](https://aistudio.google.com/app/apikey).
   
   Set it as an environment variable (Recommended):
   ```bash
   # Windows PowerShell
   $env:GEMINI_API_KEY="your-api-key-here"
   ```
   Or update the `resume_screener.py` file directly:
   ```python
   genai.configure(api_key="your-actual-api-key")
   ```

---

## 💻 Usage

Run the main script:
```bash
python resume_screener.py
```

### 1. Select Mode
You will be greeted with a menu:
```
[1] Screen single resume
[2] Screen batch (folder of resumes)
```

### 2. Select Job Role
Choose a preset or define your own:
- **Options 1-6:** Preset roles.
- **Option 7 (Custom):**
  - **Sub-option A:** Enter a title (e.g., "Marketing Manager") -> AI generates the criteria.
  - **Sub-option B:** Paste a full job description manually.

### 3. Review Results
- **Terminal:** Summary results are printed immediately.
- **Files:** Detailed reports are saved to:
  - `results/CandidateName_Date.txt` (Individual reports)
  - `screening_results.txt` (Last run summary)

---

## 📂 Project Structure

- `resume_screener.py`: The main application logic.
- `results/`: Directory housing all generated screening reports.
- `sample_resume.pdf`: A generated resume for testing purposes.

---

## 🙏 Credits

Special thanks to **Aman Kharwal** for the original "Build an AI Resume Screener" tutorial.
