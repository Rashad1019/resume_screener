"""Create a sample resume PDF for testing the AI Resume Screener"""

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

def create_sample_resume():
    c = canvas.Canvas("sample_resume.pdf", pagesize=letter)
    width, height = letter
    
    # Name
    c.setFont("Helvetica-Bold", 24)
    c.drawString(1*inch, height - 1*inch, "John Smith")
    
    # Contact Info
    c.setFont("Helvetica", 10)
    c.drawString(1*inch, height - 1.3*inch, "john.smith@email.com | (555) 123-4567 | San Francisco, CA")
    c.drawString(1*inch, height - 1.5*inch, "LinkedIn: linkedin.com/in/johnsmith | GitHub: github.com/johnsmith")
    
    # Summary
    y = height - 2*inch
    c.setFont("Helvetica-Bold", 14)
    c.drawString(1*inch, y, "PROFESSIONAL SUMMARY")
    c.line(1*inch, y - 5, width - 1*inch, y - 5)
    
    c.setFont("Helvetica", 10)
    y -= 0.3*inch
    summary = """Aspiring Data Scientist with 2 years of experience in data analysis and machine learning.
Proficient in Python, SQL, and statistical modeling. Passionate about turning data into actionable insights."""
    for line in summary.split('\n'):
        c.drawString(1*inch, y, line.strip())
        y -= 0.2*inch
    
    # Skills
    y -= 0.3*inch
    c.setFont("Helvetica-Bold", 14)
    c.drawString(1*inch, y, "TECHNICAL SKILLS")
    c.line(1*inch, y - 5, width - 1*inch, y - 5)
    
    c.setFont("Helvetica", 10)
    y -= 0.3*inch
    skills = [
        "Programming: Python (Pandas, NumPy, Scikit-Learn, Matplotlib), R, SQL",
        "Machine Learning: Linear Regression, Random Forests, K-Means Clustering, Neural Networks",
        "Tools: Jupyter Notebook, Git, Docker, Tableau, Power BI",
        "Cloud: AWS (S3, EC2), Google Cloud Platform",
        "Databases: PostgreSQL, MySQL, MongoDB"
    ]
    for skill in skills:
        c.drawString(1*inch, y, f"• {skill}")
        y -= 0.2*inch
    
    # Experience
    y -= 0.3*inch
    c.setFont("Helvetica-Bold", 14)
    c.drawString(1*inch, y, "WORK EXPERIENCE")
    c.line(1*inch, y - 5, width - 1*inch, y - 5)
    
    y -= 0.3*inch
    c.setFont("Helvetica-Bold", 11)
    c.drawString(1*inch, y, "Junior Data Analyst | TechCorp Inc.")
    c.setFont("Helvetica", 10)
    c.drawString(5*inch, y, "Jan 2023 - Present")
    
    y -= 0.25*inch
    c.setFont("Helvetica", 10)
    exp1 = [
        "• Built predictive models using Python and Scikit-Learn to forecast customer churn",
        "• Created automated data pipelines using SQL and Python, reducing report time by 40%",
        "• Developed interactive dashboards in Tableau for executive stakeholders",
        "• Collaborated with cross-functional teams to define KPIs and metrics"
    ]
    for item in exp1:
        c.drawString(1*inch, y, item)
        y -= 0.2*inch
    
    y -= 0.2*inch
    c.setFont("Helvetica-Bold", 11)
    c.drawString(1*inch, y, "Data Science Intern | StartupXYZ")
    c.setFont("Helvetica", 10)
    c.drawString(5*inch, y, "Jun 2022 - Dec 2022")
    
    y -= 0.25*inch
    exp2 = [
        "• Performed exploratory data analysis on 1M+ customer records",
        "• Implemented NLP models for sentiment analysis of customer reviews",
        "• Presented findings to leadership, influencing product roadmap decisions"
    ]
    for item in exp2:
        c.drawString(1*inch, y, item)
        y -= 0.2*inch
    
    # Education
    y -= 0.3*inch
    c.setFont("Helvetica-Bold", 14)
    c.drawString(1*inch, y, "EDUCATION")
    c.line(1*inch, y - 5, width - 1*inch, y - 5)
    
    y -= 0.3*inch
    c.setFont("Helvetica-Bold", 11)
    c.drawString(1*inch, y, "B.S. in Computer Science | University of California, Berkeley")
    c.setFont("Helvetica", 10)
    c.drawString(5.5*inch, y, "2018 - 2022")
    
    y -= 0.2*inch
    c.drawString(1*inch, y, "Relevant Coursework: Machine Learning, Statistical Analysis, Data Structures, Algorithms")
    
    # Certifications
    y -= 0.4*inch
    c.setFont("Helvetica-Bold", 14)
    c.drawString(1*inch, y, "CERTIFICATIONS")
    c.line(1*inch, y - 5, width - 1*inch, y - 5)
    
    y -= 0.3*inch
    c.setFont("Helvetica", 10)
    certs = [
        "• AWS Certified Cloud Practitioner (2024)",
        "• Google Data Analytics Professional Certificate (2023)"
    ]
    for cert in certs:
        c.drawString(1*inch, y, cert)
        y -= 0.2*inch
    
    c.save()
    print("✅ Created sample_resume.pdf")

if __name__ == "__main__":
    create_sample_resume()
