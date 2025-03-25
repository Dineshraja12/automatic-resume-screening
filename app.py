from flask import Flask, request, jsonify, render_template
import fitz  # PyMuPDF for PDF
import docx  

app = Flask(__name__)

# Function to extract text from PDF
def extract_text_from_pdf(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    text = "\n".join([page.get_text() for page in doc])
    return text

# Function to extract text from DOCX
def extract_text_from_docx(file):
    doc = docx.Document(file)
    text = "\n".join([para.text for para in doc.paragraphs])
    return text

# Keyword Matching
def keyword_matching(resume_text, keywords):
    resume_text_lower = resume_text.lower()
    matched = [kw for kw in keywords if kw.lower() in resume_text_lower]
    return matched

# Calculate Score
def calculate_score(resume_text, keywords):
    matched = keyword_matching(resume_text, keywords)
    return (len(matched) / len(keywords)) * 100 if keywords else 0

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload_resumes():
    if "resumes" not in request.files or "jobDescription" not in request.form:
        return jsonify({"error": "No files or job description uploaded"}), 400

    job_description = request.form["jobDescription"]
    jd_keywords = job_description.split()  # Simple keyword extraction from job description

    best_score = 0
    best_resume = ""
    
    # Process each uploaded resume
    for file in request.files.getlist("resumes"):
        filename = file.filename

        if filename.endswith(".pdf"):
            resume_text = extract_text_from_pdf(file)
        elif filename.endswith(".docx"):
            resume_text = extract_text_from_docx(file)
        else:
            return jsonify({"error": "Unsupported file format"}), 400

        score = calculate_score(resume_text, jd_keywords)
        
        # Check if this resume has the best score
        if score > best_score:
            best_score = score
            best_resume = filename  # Store the name of the best resume

    return jsonify({"best_score": round(best_score, 2), "best_resume": best_resume})

if __name__ == "__main__":
    app.run(debug=True)