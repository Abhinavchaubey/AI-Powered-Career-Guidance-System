# AI-Powered Career Guidance System

def get_career_recommendations(interests, skills, academic_background):
    recommendations = []

    # Normalize inputs
    interests = [i.strip().lower() for i in interests]
    skills = [s.strip().lower() for s in skills]
    academic_background = academic_background.strip().lower()

    # Rule-based logic
    if 'data' in interests or 'analysis' in skills or 'statistics' in skills:
        recommendations.append('Data Scientist')
    if 'web' in interests or 'html' in skills or 'css' in skills or 'javascript' in skills:
        recommendations.append('Web Developer')
    if 'ai' in interests or 'machine learning' in skills or 'deep learning' in skills:
        recommendations.append('AI/ML Engineer')
    if 'design' in interests or 'creativity' in skills or 'figma' in skills:
        recommendations.append('UI/UX Designer')
    if 'network' in interests or 'security' in skills or 'ethical hacking' in skills:
        recommendations.append('Cybersecurity Analyst')
    if 'cloud' in interests or 'devops' in skills or 'aws' in skills or 'azure' in skills:
        recommendations.append('Cloud Engineer')
    if 'robotics' in interests or 'automation' in skills or 'iot' in skills:
        recommendations.append('Robotics Engineer')
    if 'mobile' in interests or 'android' in skills or 'ios' in skills:
        recommendations.append('Mobile App Developer')

    if not recommendations:
        recommendations.append('Software Developer')

    return recommendations

# Sample inputs (replace with input() for interactive use)
interests = ['AI', 'Web', 'Data']
skills = ['Python', 'Machine Learning', 'HTML']
academic_background = 'Computer Science'

# Get recommendations
careers = get_career_recommendations(interests, skills, academic_background)

# Display results
print("Recommended Career Paths:")
for career in careers:
    print(f"- {career}")

# Save to file
with open("career_recommendations.txt", "w") as f:
    f.write("Career Recommendations:\n")
    for career in careers:
        f.write(f"- {career}\n")
