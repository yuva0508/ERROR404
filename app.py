from flask import Flask, render_template, request
from role_config import DOMAINS,ROLE_COMPANIES
from engine import calculate_role_scores, analyze_resume,get_preparation_level
from roadmap import ROLE_ROADMAPS
from flask import session, redirect, url_for
from database import init_db
from auth import register_user, validate_user
init_db()

app = Flask(__name__)
app.secret_key = "career_guidance_secret"

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if validate_user(username, password):
            session["user"] = username
            return redirect(url_for("home"))

        else:
            return "Invalid Credentials"

    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if register_user(username, password):
            return redirect(url_for("login"))
        else:
            return "User already exists"

    return render_template("register.html")
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

# -----------------------------------------
# HOME PAGE
# -----------------------------------------

@app.route("/")
def root():
    return redirect(url_for("login"))

@app.route("/home")
def home():
    if "user" not in session:
        return redirect(url_for("login"))

    return render_template("index.html", domains=DOMAINS, session=session)


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
    # Preparation level (S5)
    preparation_level = get_preparation_level(best_score)

    # -----------------------------------
    # ADD THIS PART (Percentage logic)
    # -----------------------------------
    max_possible_score = 150   # change this based on your scoring logic
    compatibility_percentage = (best_score / max_possible_score) * 100
    compatibility_percentage = round(compatibility_percentage, 2)
    # -----------------------------------

    # Resume analysis
    resume_analysis = analyze_resume(best_role, resume_text)
    companies = ROLE_COMPANIES.get(best_role, [])

    # Roadmap
    roadmap = ROLE_ROADMAPS.get(best_role, {})

    return render_template(
        "result.html",
        best_role=best_role,
        best_score=best_score,
        compatibility_percentage=compatibility_percentage,  # send to HTML
        role_scores=role_scores,
        resume_analysis=resume_analysis,
        roadmap=roadmap,
        preparation_level=preparation_level,
        companies=companies
    )


# -----------------------------------------
# RUN SERVER
# -----------------------------------------

if __name__ == "__main__":
    app.run(debug=True)
