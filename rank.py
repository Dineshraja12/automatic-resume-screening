resumes = ["resume1.pdf", "resume2.pdf", "resume3.pdf"]
scores = []

for resume in resumes:
    text = extract_text_from_pdf(resume)
    score = calculate_score(text, jd_keywords)
    scores.append((resume, score))

# Sorting resumes by score
sorted_resumes = sorted(scores, key=lambda x: x[1], reverse=True)

for res in sorted_resumes:
    print(f"{res[0]} - {res[1]:.2f}% Match")