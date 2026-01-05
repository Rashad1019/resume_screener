# Build an AI Resume Screener with Python & Llama 3

An AI-powered resume screening tool built with Python and Llama 3 (via Ollama). This tool helps recruiters and hiring managers quickly evaluate resumes against job descriptions using local AI analysis.

> **Note:** This project is based on the tutorial **"Build an AI Resume Screener with Python & Llama 3"** by **Aman Kharwal**. We've enhanced it with batch processing and custom job description capabilities.

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

- **3. 🤖 Local Llama 3 Integration:** 
  - Uses **Ollama** to run Llama 3 locally on your machine.
  - Private, free, and secure - no data leaves your computer.

- **4. 💾 Auto-Save & Structured Reporting:**
  - Every session saves a detailed text report to the `results/` folder.
  - Reports include Match Score, Decision, Strengths, Missing Skills, and Reasoning.

---

## 🚀 Setup

1. **Install Ollama:**
   Download from [ollama.com](https://ollama.com) and run:
   ```bash
   ollama pull llama3
   ```

2. **Install Python Libraries:**
   ```bash
   pip install ollama pymupdf
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
  - `results/CandidateName_timestamp.txt` (Individual reports)
  - `screening_results.txt` (Last run summary)

---

## 📂 Project Structure

- `resume_screener.py`: The main application logic.
- `results/`: Directory housing all generated screening reports.
- `sample_resume.pdf`: A generated resume for testing purposes.

---

## 🙏 Credits

Special thanks to **Aman Kharwal** for the original "Build an AI Resume Screener" tutorial.
