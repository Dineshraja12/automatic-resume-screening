def calculate_score(resume_text, keywords):
    matched = keyword_matching(resume_text, keywords)
    score = (len(matched) / len(keywords)) * 100  # Percentage match
    return score

resume_score = calculate_score(resume_text, jd_keywords)
print(f"Resume Score: {resume_score}%")