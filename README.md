# AI Resume Screener

An AI-powered resume screening tool built with Python and Google's Gemini API. This tool helps recruiters and hiring managers quickly evaluate resumes against job descriptions using advanced AI analysis.

## 🙏 Credits

This project is based on the excellent tutorial **"Build an AI Resume Screener with Python & Llama 3"** by **[Aman Kharwal](https://thecleverprogrammer.com/)**. The original tutorial used Ollama with Llama 3 for local inference. This version has been adapted to use **Google's Gemini API** for cloud-based AI processing.

Thank you, Aman, for the fantastic tutorial and inspiration!

## ✨ Features

- **Single Resume Screening**: Analyze one resume at a time
- **Batch Processing**: Screen multiple resumes from a folder simultaneously
- **Multiple Job Roles**: Choose from 6 preset job descriptions or create custom ones
- **AI-Generated Job Descriptions**: Just enter a role title and let AI create the JD
- **Detailed Reports**: Get match scores, strengths, missing skills, and recommendations
- **Auto-Save Results**: All screening results saved to individual files with timestamps

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- A Google Gemini API key ([Get one here](https://aistudio.google.com/app/apikey))

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/resume_screener.git
   cd resume_screener
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv .venv
   
   # Windows
   .venv\Scripts\activate
   
   # macOS/Linux
   source .venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Add your Gemini API key:**
   
   Open `resume_screener.py` and replace `"your-gemini-api-key"` on line 11 with your actual API key:
   ```python
   genai.configure(api_key="YOUR_ACTUAL_API_KEY")
   ```

### Usage

Run the main script:
```bash
python resume_screener.py
```

You'll see the main menu:
```
==================================================
      AI RESUME SCREENER
==================================================

Select mode:
  [1] Screen single resume
  [2] Screen batch (folder of resumes)
==================================================
```

## 📋 How It Works

### The Three Parts

Based on Aman Kharwal's tutorial, the screener consists of three main components:

1. **The Reader**: Uses PyMuPDF to extract text from PDF resumes
2. **The Brain**: Prompt engineering that gives the AI a "Senior Technical Recruiter" persona with 20 years of experience
3. **The Execution**: Handles input, processes resumes, and outputs structured results

### Job Role Options

The screener comes with 6 preset job descriptions:
- Junior Data Scientist
- Software Engineer
- Data Analyst
- Fintech Operations Specialist
- Product Manager
- Customer Success Manager

You can also:
- **Option A**: Enter a role title and let AI generate the job description
- **Option B**: Paste your own custom job description

### Output Format

For each resume, you'll get:
```
==================================================
         SCREENING REPORT
==================================================

Candidate: John Smith
Match Score: 85/100
Decision: INTERVIEW

Key Strengths:
   - Strong Python skills with Pandas and NumPy
   - SQL experience with PostgreSQL
   - Machine Learning project experience

Missing Skills:
   - AWS or cloud deployment experience

Reasoning: The candidate demonstrates solid technical 
fundamentals for a Junior Data Scientist role...

==================================================
```

## 📁 Project Structure

```
resume_screener/
├── resume_screener.py      # Main application
├── requirements.txt        # Python dependencies
├── sample_resume.pdf       # Sample resume for testing
├── create_sample_resume.py # Script to generate sample PDFs
├── results/                # Folder where results are saved
└── README.md               # This file
```

## 🔧 Configuration

### Changing the AI Model

The default model is `gemini-3-flash-preview`. To use a different Gemini model, edit line 14 in `resume_screener.py`:
```python
model = genai.GenerativeModel('gemini-2.0-flash')  # or another model
```

### Adding New Job Descriptions

Add new preset job descriptions in the `JOB_DESCRIPTIONS` dictionary in `resume_screener.py`.

## 📖 Original Tutorial Concepts

From Aman Kharwal's tutorial, this project teaches three critical GenAI skills:

1. **Context Window Management**: Understanding how much text (Resume + JD) fits into the prompt
2. **Structured Output**: Forcing a creative AI to produce structured JSON data
3. **Prompt Engineering**: Using personas and constraints to get better AI responses

## ⚠️ Notes

- Results are saved to the `results/` folder with unique filenames (CandidateName_timestamp.txt)
- The AI uses semantic matching - "React" matches "React.js", "ML" matches "Machine Learning"
- For best results, ensure resumes are text-based PDFs (not scanned images)

## 📝 License

This project is open source and available under the MIT License.

## 🔗 Links

- [Original Tutorial by Aman Kharwal](https://thecleverprogrammer.com/)
- [Google Gemini API Documentation](https://ai.google.dev/docs)
- [PyMuPDF Documentation](https://pymupdf.readthedocs.io/)
