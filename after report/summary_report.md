# 🧠 Summary Report: AI Resume Screener

## 🚀 The Problem
Recruiters and hiring managers spend countless hours manually reviewing resumes. This process is:
- **Time-Consuming:** Average screening time is 6-10 seconds per resume, but deep review takes minutes.
- **Inconsistent:** Human fatigue leads to missed details or biased decision-making.
- **Keyword-Dependent:** Traditional ATS systems miss "semantic matches" (e.g., rejecting "React" when looking for "React.js").

## 💡 The Solution
The **AI Resume Screener** automates the initial evaluation stage using Large Language Models (LLMs). By utilizing **Google's Gemini API**, the tool acts as a "Senior Technical Recruiter" with 20 years of experience.

It doesn't just look for keywords; it **understands context**.

### How It Works (Simplified)
1. **Read:** The tool opens a PDF resume and extracts all text using Python.
2. **Think:** It sends the resume + the exact Job Description to the AI Brain.
3. **Decide:** The AI evaluates the match based on skills, experience, and nuance.
4. **Report:** It generates a structured score (0-100), a recommendation (Interview/Reject), and a written justification.

## 🔑 Key Features & Benefits
- **Batch Processing:** Drop 50 resumes in a folder, walk away for 2 minutes, and come back to a ranked list of candidates.
- **Adaptive Screening:** Can screen for a "Data Scientist" one minute and a "Marketing Manager" the next using Custom Job Descriptions.
- **Standardized Scoring:** Every candidate is judged against the exact same criteria, reducing unconscious bias.

## 📊 Business Impact
- **90% Faster Screening:** Process dozens of resumes in the time it takes to read one.
- **Better Matches:** Finds candidates that keyword searches miss (e.g., inferring "Leadership" from "Managed a team of 5").
- **Instant Documentation:** Automatically creates a written report for every candidate for compliance and review.
