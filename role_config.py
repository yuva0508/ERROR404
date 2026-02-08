# ============================================
# ROLE CONFIGURATION FILE
# ============================================

# --------------------------------------------
# DOMAIN DEFINITIONS
# --------------------------------------------

DOMAINS = {
    "dsa": "Data Structures & Algorithms",
    "web_dev": "Web Development",
    "ml": "Machine Learning",
    "cloud": "Cloud Computing",
    "cybersecurity": "Cybersecurity",
    "uiux": "UI / UX Design",
    "marketing": "Marketing",
    "finance": "Finance",
    "communication": "Communication",
    "leadership": "Leadership"
}


# --------------------------------------------
# SKILL LEVEL NUMERIC MAPPING
# --------------------------------------------

LEVEL_SCORES = {
    "nothing": 0,
    "beginner": 1,
    "average": 2,
    "good": 3,
    "awesome": 4
}


# --------------------------------------------
# ROLE WEIGHT MATRIX
# --------------------------------------------

ROLE_WEIGHTS = {

    "Software Engineer": {
        "dsa": 5, "web_dev": 3, "ml": 2, "cloud": 3,
        "cybersecurity": 2, "uiux": 1, "marketing": 0,
        "finance": 0, "communication": 3, "leadership": 2
    },

    "Full Stack Developer": {
        "dsa": 3, "web_dev": 5, "ml": 1, "cloud": 3,
        "cybersecurity": 2, "uiux": 3, "marketing": 1,
        "finance": 0, "communication": 3, "leadership": 2
    },

    "Data Scientist": {
        "dsa": 3, "web_dev": 1, "ml": 5, "cloud": 2,
        "cybersecurity": 1, "uiux": 1, "marketing": 1,
        "finance": 2, "communication": 3, "leadership": 2
    },

    "Machine Learning Engineer": {
        "dsa": 4, "web_dev": 2, "ml": 5, "cloud": 3,
        "cybersecurity": 1, "uiux": 1, "marketing": 0,
        "finance": 1, "communication": 3, "leadership": 2
    },

    "Cloud Engineer": {
        "dsa": 2, "web_dev": 2, "ml": 1, "cloud": 5,
        "cybersecurity": 3, "uiux": 0, "marketing": 0,
        "finance": 1, "communication": 3, "leadership": 2
    },

    "DevOps Engineer": {
        "dsa": 3, "web_dev": 3, "ml": 1, "cloud": 5,
        "cybersecurity": 3, "uiux": 0, "marketing": 0,
        "finance": 0, "communication": 3, "leadership": 3
    },

    "Cybersecurity Analyst": {
        "dsa": 2, "web_dev": 1, "ml": 1, "cloud": 3,
        "cybersecurity": 5, "uiux": 0, "marketing": 0,
        "finance": 1, "communication": 3, "leadership": 2
    },

    "UI/UX Designer": {
        "dsa": 0, "web_dev": 2, "ml": 0, "cloud": 0,
        "cybersecurity": 0, "uiux": 5, "marketing": 3,
        "finance": 0, "communication": 4, "leadership": 2
    },

    "Product Manager": {
        "dsa": 1, "web_dev": 2, "ml": 1, "cloud": 1,
        "cybersecurity": 1, "uiux": 3, "marketing": 4,
        "finance": 3, "communication": 5, "leadership": 5
    },

    "Business Analyst": {
        "dsa": 1, "web_dev": 1, "ml": 2, "cloud": 1,
        "cybersecurity": 0, "uiux": 1, "marketing": 3,
        "finance": 4, "communication": 4, "leadership": 3
    },

    "Digital Marketing Strategist": {
        "dsa": 0, "web_dev": 2, "ml": 1, "cloud": 0,
        "cybersecurity": 0, "uiux": 3, "marketing": 5,
        "finance": 2, "communication": 5, "leadership": 3
    },

    "AI Product Strategist": {
        "dsa": 2, "web_dev": 2, "ml": 4, "cloud": 2,
        "cybersecurity": 1, "uiux": 2, "marketing": 4,
        "finance": 3, "communication": 5, "leadership": 5
    }
}


# --------------------------------------------
# RESUME KEYWORD MATCHING
# --------------------------------------------

ROLE_REQUIRED_SKILLS = {

    "Software Engineer": [
        "python", "java", "c++", "data structures",
        "algorithms", "git", "sql", "api", "system design"
    ],

    "Full Stack Developer": [
        "html", "css", "javascript", "react",
        "node", "flask", "django", "api",
        "mongodb", "sql"
    ],

    "Data Scientist": [
        "python", "machine learning", "pandas",
        "numpy", "statistics", "sql",
        "data visualization", "tensorflow"
    ],

    "Machine Learning Engineer": [
        "python", "deep learning", "tensorflow",
        "pytorch", "model deployment",
        "mlops", "docker"
    ],

    "Cloud Engineer": [
        "aws", "azure", "gcp",
        "docker", "kubernetes",
        "linux", "cloud architecture"
    ],

    "DevOps Engineer": [
        "ci/cd", "docker", "kubernetes",
        "jenkins", "linux",
        "aws", "automation"
    ],

    "Cybersecurity Analyst": [
        "networking", "cybersecurity",
        "penetration testing", "linux",
        "encryption", "firewalls"
    ],

    "UI/UX Designer": [
        "figma", "ui", "ux",
        "prototyping", "wireframing",
        "design thinking"
    ],

    "Product Manager": [
        "product strategy", "roadmap",
        "agile", "scrum",
        "stakeholder management",
        "market research"
    ],

    "Business Analyst": [
        "excel", "sql", "power bi",
        "data analysis", "business strategy",
        "requirements gathering"
    ],

    "Digital Marketing Strategist": [
        "seo", "content marketing",
        "google analytics", "social media",
        "branding", "campaign strategy"
    ],

    "AI Product Strategist": [
        "ai", "machine learning",
        "product strategy",
        "data analysis",
        "market research",
        "roadmapping"
    ]
}
ROLE_DESCRIPTIONS = {
    "Software Engineer": "Designs and builds scalable software systems.",
    "Data Scientist": "Analyzes data to extract insights and build models.",
}

