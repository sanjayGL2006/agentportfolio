import os
from flask import Flask, render_template, send_from_directory, request, jsonify

app = Flask(__name__, static_folder=".", static_url_path="")

# Predefined Q&A Knowledge Base for Sanjay G. L.
KNOWLEDGE_BASE = {
    "who are you": "I am Sanjay's personal AI Portfolio Assistant! I can answer questions about Sanjay G. L.'s skills, projects, certificates, and background.",
    "tell me about yourself": "Sanjay G. L. is a BCA student at PES Institute of Advanced Management Studies, Shivamogga, Karnataka. He is a Full Stack Developer, AI Enthusiast, and NSS Volunteer who builds scalable web applications and AI tools.",
    "skills": "Sanjay's core technical skills include HTML5, CSS3, JavaScript, Python, C, C++, Java, PHP, SQL, MySQL, Flask, Node.js, Git, GitHub, Linux, and AI Prompt Engineering.",
    "programming languages": "Sanjay is proficient in Python, JavaScript, C, C++, Java, PHP, and SQL.",
    "projects": "Sanjay has built 23+ projects including RupeeTrack (Expense Tracker), Pure Weaves E-Commerce, Digital Board Duel, GrabNotes AI, Spy Detect Pro, AI Agent (Google AI API), Kai Assistant, and Placement Portals.",
    "certificates": "Sanjay has earned 102+ verified certificates across AI, Python, Cybersecurity, Web Development, Government programs, and HackerRank (Python, SQL, JavaScript, React, Problem Solving).",
    "future goals": "Sanjay aims to excel as a Senior Full Stack Engineer & AI Developer, building intelligent software solutions that solve real-world problems.",
    "technologies": "Sanjay works with HTML, CSS, JavaScript, React, TypeScript, Python, Flask, MySQL, MongoDB, Google Cloud Run, Git, VS Code, and Cursor AI.",
    "freelance": "Yes! Sanjay is open to freelance web development, AI workflow integration, and software projects, as well as full-time internships.",
    "contact": "You can contact Sanjay via email at sanjaygl2006@gmail.com, phone at +91 81239 81877, or connect on LinkedIn and GitHub.",
    "from": "Sanjay is from Shivamogga, Karnataka, India.",
    "why hire": "Sanjay brings strong problem-solving skills, hands-on experience in full-stack web and AI development, 102+ certifications, a passion for clean code, and a proven track record of building production-ready projects."
}

@app.route("/")
def index():
    return send_from_directory(".", "index.html")

@app.route("/<path:path>")
def serve_static(path):
    if os.path.exists(path):
        return send_from_directory(".", path)
    return send_from_directory(".", "index.html")

@app.route("/api/about", methods=["GET"])
def get_about():
    return jsonify({
        "name": "Sanjay G. L.",
        "role": "BCA Student & Full Stack Developer",
        "location": "Shivamogga, Karnataka, India",
        "email": "sanjaygl2006@gmail.com",
        "phone": "+91 81239 81877",
        "skills": [
            "HTML5", "CSS3", "JavaScript", "TypeScript", "Python", "Flask",
            "C", "C++", "Java", "SQL", "MySQL", "Git", "GitHub", "AI Prompt Engineering"
        ],
        "total_projects": 23,
        "total_certificates": 102,
        "freelance_available": True
    })

@app.route("/api/contact", methods=["POST"])
def handle_contact():
    data = request.get_json() or request.form
    name = data.get("name", "Visitor")
    email = data.get("email", "")
    message = data.get("message", "")
    print(f"[CONTACT FORM] From: {name} ({email}) | Message: {message}")
    return jsonify({"status": "success", "message": f"Thank you, {name}! Your message has been received."})

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json() or {}
    message = str(data.get("message", "")).lower().strip()
    
    if not message:
        return jsonify({"reply": "Please ask me a question!"})

    for key, answer in KNOWLEDGE_BASE.items():
        if key in message:
            return jsonify({"reply": answer})

    if "hire" in message:
        return jsonify({"reply": KNOWLEDGE_BASE["why hire"]})
    if "skill" in message or "know" in message:
        return jsonify({"reply": KNOWLEDGE_BASE["skills"]})
    if "project" in message or "built" in message:
        return jsonify({"reply": KNOWLEDGE_BASE["projects"]})
    if "certif" in message:
        return jsonify({"reply": KNOWLEDGE_BASE["certificates"]})
    if "email" in message or "phone" in message or "reach" in message:
        return jsonify({"reply": KNOWLEDGE_BASE["contact"]})

    return jsonify({
        "reply": "I'm sorry, I don't have that information yet. Please contact Sanjay directly at sanjaygl2006@gmail.com."
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
