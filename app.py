from flask import Flask, render_template, request
from role_config import DOMAINS
from engine import (
    calculate_role_compatibility,
    classify_readiness,
    analyze_skill_gaps
)
from roadmap import ROLE_ROADMAPS

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", domains=DOMAINS)


@app.route('/analyze', methods=['POST'])
def analyze():

    user_inputs = {}

    for domain in DOMAINS:
        level = request.form.get(domain)
        user_inputs[domain] = level

    # Calculate compatibility
    results = calculate_role_compatibility(user_inputs)

    top_role = results[0]
    readiness = classify_readiness(top_role[1])

    # Strength & weakness analysis
    strengths, weaknesses = analyze_skill_gaps(user_inputs)

    # Get roadmap
    roadmap = ROLE_ROADMAPS.get(top_role[0], {})

    # Personalize focus level
    if readiness == "Highly Ready":
        focus_level = "Advanced"
    elif readiness == "Moderately Ready":
        focus_level = "Intermediate"
    else:
        focus_level = "Foundation"

    return render_template(
        "result.html",
        results=results,
        top_role=top_role,
        readiness=readiness,
        strengths=strengths,
        weaknesses=weaknesses,
        roadmap=roadmap,
        focus_level=focus_level
    )


if __name__ == '__main__':
    app.run(debug=True)
