# Career Guidance System

# 🎓 Career Role Analyser

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Flask](https://img.shields.io/badge/Flask-Web%20App-green)
![HTML/CSS](https://img.shields.io/badge/Frontend-HTML%2FCSS%2FJS-orange)
![Status](https://img.shields.io/badge/Project-Active-success)

**Career Role Analyser** is an intelligent **Student Career Guidance and Resume Analyzer System** that helps students discover the most suitable career roles based on their **skills, interests, and academic background**. It also provides a **personalized learning roadmap**, evaluates resume readiness, and gives insights into companies hiring for the selected roles.

---

## 🚀 Features

- **Career Role Prediction** – Suggests best matching roles based on your skills  
- **Top 3 Role Recommendations** – Provides multiple career options  
- **Resume Analysis** – Highlights matched and missing skills in your resume  
- **Compatibility Score & Progress Bar** – Shows your readiness for each role  
- **Preparation Level Benchmark** – Beginner, Intermediate, Advanced, Placement Ready  
- **Personalized Roadmap** – Step-by-step learning path with free/premium resources  
- **Companies Hiring** – Shows companies that recruit for the selected role  
- **Modern UI** – Clean and professional interface

---

## 🖥️ Technology Stack

**Frontend:** HTML, CSS, Jinja2 Templates  
**Backend:** Python, Flask  
**Tools:** VS Code, Git & GitHub  

---

## 📂 Project Structure
career_project/
│
├── app.py # Main Flask application
├── engine.py # Role scoring and resume analyzer
├── role_config.py # Skill levels, roles, and required skills
├── roadmap.py # Learning roadmap for each role
│
├── templates/
│ ├── index.html # Input form
│ └── result.html # Output with role, roadmap, and progress bars
│
└── static/
└── style.css # Optional styling


---

## ⚙️ Installation & Setup

# Step 1: Clone the Repository

git clone https://github.com/your-username/career-role-analyser.git
cd career-role-analyser

# Step 2: Install Dependencies
pip install flask

# Step 3: Run the Project
python app.py

# Step 4: Open in Browser
http://127.0.0.1:5000

🎯 How It Works

Students select their skill levels across domains.

System calculates role compatibility scores.

Displays best matching career role and top 3 roles with progress bars.

Analyzes resume for matched and missing skills.

Shows preparation level and companies hiring for the role.

Provides personalized learning roadmap with projects and resources.

📊 Example Output

Best Role: Software Engineer

Compatibility Score: 82%

Top 3 Roles: Software Engineer – 82%, Full Stack Developer – 76%, DevOps Engineer – 65%

Resume Match:

Matched Skills: Python, Git, SQL

Missing Skills: API, System Design

Preparation Level: Advanced

Companies Hiring: Google, Microsoft, Amazon

Roadmap: Build projects, learn Data Structures, system design tutorials

💡 Future Improvements

AI-based resume parsing (PDF/DOCX)

Skill gap visualizations and charts

Login system with progress tracking

Interactive interview preparation module

Cloud deployment for online access

🤝 Contributing

Contributions are welcome!

Fork the repository

Create a branch (git checkout -b feature-name)

Make your changes

Commit (git commit -m "Add feature")

Push (git push origin feature-name)

Create a Pull Request

📜 License

This project is for educational and competition purposes.

