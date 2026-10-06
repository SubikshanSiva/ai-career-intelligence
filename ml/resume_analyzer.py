from skills import SKILLS
from job_roles import JOB_ROLES


def analyze_resume(resume):

    resume = resume.lower()

    found_skills = []

    for skill in SKILLS:
        if skill in resume:
            found_skills.append(skill)

    return found_skills


def find_skill_gap(found_skills, required_skills):

    missing_skills = []

    for skill in required_skills:
        if skill not in found_skills:
            missing_skills.append(skill)

    return missing_skills


resume = input("Paste your resume text:\n")

role = input("\nEnter target job role:\n").lower()

if role not in JOB_ROLES:
    print("\nJob role not available.")
else:

    detected_skills = analyze_resume(resume)

    required_skills = JOB_ROLES[role]

    missing_skills = find_skill_gap(
        detected_skills,
        required_skills
    )

    print("\nDetected Skills:")

    for skill in detected_skills:
        print("-", skill)

    print("\nMissing Skills:")

    for skill in missing_skills:
        print("-", skill)