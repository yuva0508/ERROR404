# engine.py

from role_config import LEVEL_SCORES, ROLE_WEIGHTS


def calculate_role_compatibility(user_inputs):

    numeric_scores = {}

    for domain, level in user_inputs.items():
        numeric_scores[domain] = LEVEL_SCORES.get(level, 0)

    role_scores = {}

    for role, weights in ROLE_WEIGHTS.items():
        total_score = 0
        max_possible = 0

        for domain, weight in weights.items():
            user_score = numeric_scores.get(domain, 0)

            total_score += user_score * weight
            max_possible += 4 * weight

        compatibility_percentage = (total_score / max_possible) * 100
        role_scores[role] = round(compatibility_percentage, 2)

    sorted_roles = sorted(
        role_scores.items(),
        key=lambda x: x[1],
        reverse=True
    )

    return sorted_roles


def classify_readiness(score):
    if score >= 80:
        return "Highly Ready"
    elif score >= 60:
        return "Moderately Ready"
    elif score >= 40:
        return "Needs Improvement"
    else:
        return "Beginner Level"


def analyze_skill_gaps(user_inputs):

    numeric_scores = {}

    for domain, level in user_inputs.items():
        numeric_scores[domain] = LEVEL_SCORES.get(level, 0)

    sorted_domains = sorted(
        numeric_scores.items(),
        key=lambda x: x[1],
        reverse=True
    )

    strengths = [d[0] for d in sorted_domains if d[1] >= 3]
    weaknesses = [d[0] for d in sorted_domains if d[1] <= 2]

    return strengths[:3], weaknesses[:3]
