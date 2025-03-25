def keyword_matching(resume_text, keywords):
    resume_text_lower = resume_text.lower()
    matched_keywords = [kw for kw in keywords if kw.lower() in resume_text_lower]
    return matched_keywords

# Example usage
resume_text = extract_text_from_pdf("resume.pdf")
jd_keywords = ["Python", "Machine Learning", "Django", "SQL"]

matched = keyword_matching(resume_text, jd_keywords)
print("Matched Keywords:", matched)