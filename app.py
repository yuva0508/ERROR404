from flask import Flask, render_template, request
from role_config import DOMAINS
from engine import calculate_role_scores, analyze_resume
from roadmap import ROLE_ROADMAPS

app = Flask(__name__)


# -----------------------------------------
# HOME PAGE
# -----------------------------------------

@app.route("/")
def home():
    return render_template("index.html", domains=DOMAINS)


# -----------------------------------------
# ANALYZE ROUTE
# -----------------------------------------

@app.route("/analyze", methods=["POST"])
def analyze():

    # Collect skill levels from form
    user_skills = {}

    for domain in DOMAINS.keys():
        level = request.form.get(domain)
        user_skills[domain] = level

    # Resume text (optional)
    resume_text = request.form.get("resume", "").lower()

    # Calculate role compatibility
    role_scores = calculate_role_scores(user_skills)

    # Get best role
    best_role = max(role_scores, key=role_scores.get)
    best_score = role_scores[best_role]

    # -----------------------------------
    # ADD THIS PART (Percentage logic)
    # -----------------------------------
    max_possible_score = 150   # change this based on your scoring logic
    compatibility_percentage = (best_score / max_possible_score) * 100
    compatibility_percentage = round(compatibility_percentage, 2)
    # -----------------------------------

    # Resume analysis
    resume_analysis = analyze_resume(best_role, resume_text)

    # Roadmap
    roadmap = ROLE_ROADMAPS.get(best_role, {})

    return render_template(
        "result.html",
        best_role=best_role,
        best_score=best_score,
        compatibility_percentage=compatibility_percentage,  # send to HTML
        role_scores=role_scores,
        resume_analysis=resume_analysis,
        roadmap=roadmap
    )


# -----------------------------------------
# RUN SERVER
# -----------------------------------------

if __name__ == "__main__":
    app.run(debug=True)
