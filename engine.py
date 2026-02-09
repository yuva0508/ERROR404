# ============================================
# ENGINE LOGIC
# ============================================

from role_config import LEVEL_SCORES, ROLE_WEIGHTS, ROLE_REQUIRED_SKILLS


# --------------------------------------------
# ROLE SCORING ENGINE
# --------------------------------------------

def calculate_role_scores(user_skills):

    role_scores = {}

    for role, weights in ROLE_WEIGHTS.items():

        total_score = 0

        for domain, weight in weights.items():

            level = user_skills.get(domain, "nothing")
            numeric_level = LEVEL_SCORES.get(level, 0)

            total_score += numeric_level * weight

        role_scores[role] = total_score

    return role_scores


# --------------------------------------------
# RESUME ANALYZER
# --------------------------------------------

def analyze_resume(role, resume_text):

    required_skills = ROLE_REQUIRED_SKILLS.get(role, [])

    matched = []
    missing = []

    for skill in required_skills:
        if skill.lower() in resume_text:
            matched.append(skill)
        else:
            missing.append(skill)

    if len(required_skills) == 0:
        match_percentage = 0
    else:
        match_percentage = int((len(matched) / len(required_skills)) * 100)

    return {
        "matched_skills": matched,
        "missing_skills": missing,
        "match_percentage": match_percentage
    }
# --------------------------------------------
# PREPARATION LEVEL BENCHMARK (S5)
# Works with percentage scores (0–100)
# --------------------------------------------

def get_preparation_level(percentage):

    if percentage < 40:
        return "Beginner"
    elif percentage < 60:
        return "Intermediate"
    elif percentage < 80:
        return "Advanced"
    else:
        return "Placement Ready"
