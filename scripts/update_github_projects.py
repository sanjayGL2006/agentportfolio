import json

repos_info = [
    {
        "id": 101,
        "name": "spvm3-spend-tracker",
        "title": "SPVM³ Spend Tracker",
        "tagline": "Fast, responsive finance and expense management dashboard.",
        "desc": "Fast, responsive finance and expense management dashboard built with React, Recharts, and FastAPI for SPVM³ Tech Solution.",
        "tech": ["React", "FastAPI", "Recharts", "Python", "JavaScript", "Tailwind CSS"],
        "category": "Management & Enterprise Systems",
        "github": "https://github.com/sanjayGL2006/spvm3-spend-tracker",
        "icon": "fa-wallet",
        "year": 2026,
        "status": "Completed"
    },
    {
        "id": 102,
        "name": "SPVM3-Blog",
        "title": "SPVM³ Engineering Blog",
        "tagline": "Full-stack React & FastAPI technical blog engine.",
        "desc": "Full-stack React & FastAPI engine showcasing real-world engineering logs on real-time chat, anti-cheat mechanisms, and AI prompt engineering with load-more pagination.",
        "tech": ["React", "FastAPI", "Python", "JavaScript", "CSS3"],
        "category": "Web Applications & Portals",
        "github": "https://github.com/sanjayGL2006/SPVM3-Blog",
        "icon": "fa-newspaper",
        "year": 2026,
        "status": "Completed"
    },
    {
        "id": 103,
        "name": "spvm3-player",
        "title": "SPVM³ Music Player",
        "tagline": "Full-stack glassmorphic music player with local library sync.",
        "desc": "Full-stack modern music player built with React 18, Vite, and FastAPI featuring automatic local library sync, ID3 metadata & album art extraction, sleek glassmorphic UI, and audio visualizer.",
        "tech": ["React 18", "Vite", "FastAPI", "Python", "JavaScript", "Web Audio API"],
        "category": "Tools, Systems & Utilities",
        "github": "https://github.com/sanjayGL2006/spvm3-player",
        "icon": "fa-music",
        "year": 2026,
        "status": "Completed"
    },
    {
        "id": 104,
        "name": "spvm3-api-platform",
        "title": "SPVM³ API Platform",
        "tagline": "Multi-user Flask & MySQL backend for API keys and developer knowledge.",
        "desc": "Multi-user Flask & MySQL backend for managing API keys and serving programming knowledge via REST APIs. Includes built-in user dashboard and admin panel.",
        "tech": ["Python", "Flask", "MySQL", "REST API", "SQLAlchemy", "JWT"],
        "category": "Tools, Systems & Utilities",
        "github": "https://github.com/sanjayGL2006/spvm3-api-platform",
        "icon": "fa-key",
        "year": 2026,
        "status": "Completed"
    },
    {
        "id": 105,
        "name": "image-to-text-converter",
        "title": "Image to Text OCR Converter",
        "tagline": "Extract text from photos and convert into editable documents.",
        "desc": "Web application that extracts text from photos and documents using optical character recognition (OCR) and converts them into editable formats.",
        "tech": ["Python", "Flask", "Tesseract OCR", "OpenCV", "JavaScript", "HTML5"],
        "category": "Tools, Systems & Utilities",
        "github": "https://github.com/sanjayGL2006/image-to-text-converter",
        "icon": "fa-file-image",
        "year": 2026,
        "status": "Completed"
    },
    {
        "id": 106,
        "name": "cyber-response-platform",
        "title": "Cyber Security Incident Response Platform",
        "tagline": "Full-stack platform for tracking & resolving security incidents.",
        "desc": "Full-stack web application for tracking, managing, and resolving cybersecurity incident tickets with real-time severity triage.",
        "tech": ["JavaScript", "React", "Node.js", "Express", "MongoDB", "CSS3"],
        "category": "Tools, Systems & Utilities",
        "github": "https://github.com/sanjayGL2006/cyber-response-platform",
        "icon": "fa-shield-halved",
        "year": 2026,
        "status": "Completed"
    },
    {
        "id": 107,
        "name": "student-htr-studio",
        "title": "Student HTR Studio",
        "tagline": "Classroom-scale Handwritten Text Recognition pipeline with TrOCR & OpenCV.",
        "desc": "Classroom-scale Handwritten Text Recognition (HTR) pipeline using TrOCR, OpenCV line segmentation, NLP grammar correction, and interactive React Flow node canvas.",
        "tech": ["Python", "TrOCR", "OpenCV", "PyTorch", "React", "React Flow", "FastAPI"],
        "category": "AI & Machine Learning",
        "github": "https://github.com/sanjayGL2006/student-htr-studio",
        "icon": "fa-pen-nib",
        "year": 2026,
        "status": "Completed"
    },
    {
        "id": 108,
        "name": "malicious-url-detector",
        "title": "Malicious URL Detector",
        "tagline": "Random Forest ML model classifying malicious vs benign URLs.",
        "desc": "Lightweight Flask web application that extracts lexical features from URLs and uses a Random Forest ML model to classify them as malicious or benign.",
        "tech": ["Python", "Flask", "Scikit-learn", "Random Forest", "Pandas", "JavaScript"],
        "category": "AI & Machine Learning",
        "github": "https://github.com/sanjayGL2006/malicious-url-detector",
        "icon": "fa-bug",
        "year": 2026,
        "status": "Completed"
    },
    {
        "id": 109,
        "name": "smart-voice-notes",
        "title": "Smart Voice Notes AI",
        "tagline": "Voice note transcription & summary using Whisper & Claude.",
        "desc": "Full-stack web app that transcribes voice notes using OpenAI Whisper and generates summaries, tags, and action items using Claude via FastAPI and React.",
        "tech": ["React", "FastAPI", "Whisper", "Claude API", "Python", "JavaScript"],
        "category": "AI & Machine Learning",
        "github": "https://github.com/sanjayGL2006/smart-voice-notes",
        "icon": "fa-microphone",
        "year": 2026,
        "status": "Completed"
    },
    {
        "id": 110,
        "name": "smart-parking-system",
        "title": "Smart Parking Detection System",
        "tagline": "Computer vision parking slot availability tracker using OpenCV.",
        "desc": "Full-stack computer vision application to detect available parking slots using OpenCV, Python, and React with live status overlays.",
        "tech": ["Python", "OpenCV", "Flask", "React", "NumPy", "JavaScript"],
        "category": "AI & Machine Learning",
        "github": "https://github.com/sanjayGL2006/smart-parking-system",
        "icon": "fa-square-parking",
        "year": 2026,
        "status": "Completed"
    },
    {
        "id": 111,
        "name": "ai-paper-analyzer",
        "title": "AI Research Paper Analyzer",
        "tagline": "Analyze, summarize, and chat with academic research papers.",
        "desc": "Full-stack web app that uses AI to analyze, summarize, and chat with academic research papers. Built with React, FastAPI, and Claude.",
        "tech": ["React", "FastAPI", "Claude API", "PyPDF", "Python", "JavaScript"],
        "category": "AI & Machine Learning",
        "github": "https://github.com/sanjayGL2006/ai-paper-analyzer",
        "icon": "fa-book-bookmark",
        "year": 2026,
        "status": "Completed"
    },
    {
        "id": 112,
        "name": "spvm3-quiz-app",
        "title": "SPVM³ Secure Anti-Cheat Quiz App",
        "tagline": "Anti-cheat window focus monitoring quiz platform.",
        "desc": "Secure, timed quiz application that monitors window focus and tab switching to prevent cheating. Built with React, Flask, and SQLite.",
        "tech": ["React", "Flask", "SQLite", "Python", "JavaScript", "CSS3"],
        "category": "Web Applications & Portals",
        "github": "https://github.com/sanjayGL2006/spvm3-quiz-app",
        "icon": "fa-graduation-cap",
        "year": 2026,
        "status": "Completed"
    },
    {
        "id": 113,
        "name": "SPVM3-placement-hub-v2",
        "title": "SPVM³ Placement Hub v2",
        "tagline": "Full-stack campus placement & recruitment management suite.",
        "desc": "Full-stack placement management system streamlining student registrations, company drives, ATS scoring, and interview scheduling.",
        "tech": ["TypeScript", "React", "Node.js", "Express", "PostgreSQL", "Tailwind CSS"],
        "category": "Management & Enterprise Systems",
        "github": "https://github.com/sanjayGL2006/SPVM3-placement-hub-v2",
        "icon": "fa-briefcase",
        "year": 2026,
        "status": "Completed"
    },
    {
        "id": 114,
        "name": "placement-pro-SPVM3",
        "title": "Placement Pro SPVM³",
        "tagline": "Campus Recruitment & Placement System with Docker & Kubernetes.",
        "desc": "Smart College Placement & Campus Recruitment Management System built with Python Flask, PHP, Docker, Kubernetes & Vercel.",
        "tech": ["Python", "Flask", "PHP", "Docker", "Kubernetes", "MySQL"],
        "category": "Management & Enterprise Systems",
        "github": "https://github.com/sanjayGL2006/placement-pro-SPVM3",
        "icon": "fa-building-user",
        "year": 2026,
        "status": "Completed"
    },
    {
        "id": 115,
        "name": "otp-signup",
        "title": "OTP Email Authentication Module",
        "tagline": "Flask signup with email OTP verification & secure auth.",
        "desc": "Flask app with user signup, email OTP verification, and login — built with SQLite, Jinja2, and secure credential hashing.",
        "tech": ["Python", "Flask", "SQLite", "SMTP Email", "Jinja2", "HTML5"],
        "category": "Tools, Systems & Utilities",
        "github": "https://github.com/sanjayGL2006/otp-signup",
        "icon": "fa-envelope-circle-check",
        "year": 2026,
        "status": "Completed"
    },
    {
        "id": 116,
        "name": "SPVM3-code-notes",
        "title": "SPVM³ Code & Tech Notes Hub",
        "tagline": "Interactive computer science guides for 20+ technologies.",
        "desc": "Comprehensive Computer Science & Programming Notes Hub featuring interactive guides for 20+ technologies, code references, and an integrated certificate verification system.",
        "tech": ["HTML5", "CSS3", "JavaScript", "Markdown", "JSON"],
        "category": "Web Applications & Portals",
        "github": "https://github.com/sanjayGL2006/SPVM3-code-notes",
        "icon": "fa-book-open-reader",
        "year": 2026,
        "status": "Completed"
    },
    {
        "id": 117,
        "name": "scanner-files-",
        "title": "Browser-Based Antivirus File Scanner",
        "tagline": "Client-side signature matching & static heuristic file analysis.",
        "desc": "Self-contained, browser-based file scanner combining hash-signature matching and static heuristics (double extensions, suspicious script patterns, entropy checks) to flag threat files.",
        "tech": ["HTML5", "JavaScript", "CryptoJS", "CSS3", "Web Workers"],
        "category": "Tools, Systems & Utilities",
        "github": "https://github.com/sanjayGL2006/scanner-files-",
        "icon": "fa-shield-virus",
        "year": 2026,
        "status": "Completed"
    },
    {
        "id": 118,
        "name": "spvm3-chat",
        "title": "SPVM³ Real-Time WebSocket Chat",
        "tagline": "High-performance real-time messaging with WebSockets & FastAPI.",
        "desc": "SPVM3 Chat: A high-performance real-time chat app featuring instant messaging, multiple chat rooms, typing indicators, and live user presence powered by WebSockets and FastAPI.",
        "tech": ["JavaScript", "FastAPI", "WebSockets", "Python", "React", "CSS3"],
        "category": "Web Applications & Portals",
        "github": "https://github.com/sanjayGL2006/spvm3-chat",
        "icon": "fa-comments",
        "year": 2026,
        "status": "Completed"
    },
    {
        "id": 119,
        "name": "social-analytics-ui",
        "title": "PulseBoard — Social Analytics Dashboard",
        "tagline": "Modern social media analytics dashboard built with React & Recharts.",
        "desc": "PulseBoard: A modern social media analytics dashboard built with React, FastAPI, and Recharts. Features follower growth tracking, engagement metrics, and recent post feeds.",
        "tech": ["React", "FastAPI", "Recharts", "JavaScript", "Tailwind CSS"],
        "category": "Management & Enterprise Systems",
        "github": "https://github.com/sanjayGL2006/social-analytics-ui",
        "icon": "fa-chart-line",
        "year": 2026,
        "status": "Completed"
    },
    {
        "id": 120,
        "name": "-SPVM3-reelfind-react-fastapi",
        "title": "ReelFind — Movie & TV Discovery App",
        "tagline": "Full-stack movie discovery platform with React & FastAPI.",
        "desc": "A full-stack movie and TV show discovery app built with React and FastAPI, integrating TMDB APIs, rating filters, and trailer modal previews.",
        "tech": ["React", "FastAPI", "Python", "JavaScript", "TMDB API"],
        "category": "Web Applications & Portals",
        "github": "https://github.com/sanjayGL2006/-SPVM3-reelfind-react-fastapi",
        "icon": "fa-film",
        "year": 2026,
        "status": "Completed"
    },
    {
        "id": 121,
        "name": "spvm3-task-app",
        "title": "SPVM³ Kanban Task Manager",
        "tagline": "Interactive drag-and-drop Kanban task app with FastAPI backend.",
        "desc": "SPVM³ Task App — A sleek, intuitive Kanban task manager featuring interactive drag-and-drop columns, priority indicators, and REST API integration with FastAPI & React.",
        "tech": ["React", "FastAPI", "Python", "JavaScript", "HTML5 Drag & Drop"],
        "category": "Tools, Systems & Utilities",
        "github": "https://github.com/sanjayGL2006/spvm3-task-app",
        "icon": "fa-list-check",
        "year": 2026,
        "status": "Completed"
    },
    {
        "id": 122,
        "name": "sentry-cyber-intel",
        "title": "Sentry Cyber Intel Platform",
        "tagline": "Multi-agent AI cybersecurity intelligence with CrewAI & Groq.",
        "desc": "Multi-agent AI cybersecurity intelligence platform powered by CrewAI, Groq & Exa for automated threat intelligence research, CVE triage, and risk assessment.",
        "tech": ["Python", "CrewAI", "Groq API", "Exa API", "Flask", "React"],
        "category": "AI & Machine Learning",
        "github": "https://github.com/sanjayGL2006/sentry-cyber-intel",
        "icon": "fa-user-secret",
        "year": 2026,
        "status": "Completed"
    },
    {
        "id": 123,
        "name": "spvm3-code-editor",
        "title": "SPVM³ Desktop IDE Engine",
        "tagline": "Local-first desktop IDE built on Electron, React & Monaco Editor.",
        "desc": "Modular, local-first desktop IDE built on Electron, React & Monaco. Features multi-language runners (Python, Java, C/C++), A-Z file support, and Extensions Marketplace.",
        "tech": ["Electron", "React", "Monaco Editor", "Node.js", "JavaScript"],
        "category": "Tools, Systems & Utilities",
        "github": "https://github.com/sanjayGL2006/spvm3-code-editor",
        "icon": "fa-code",
        "year": 2026,
        "status": "Completed"
    },
    {
        "id": 124,
        "name": "smart-attendance-yolo",
        "title": "Smart Attendance System (YOLOv8)",
        "tagline": "Automated classroom attendance tracker using custom YOLOv8.",
        "desc": "Real-time automated classroom attendance tracker powered by custom YOLOv8 computer vision, Flask REST API, MySQL, and an interactive React teacher dashboard.",
        "tech": ["Python", "YOLOv8", "OpenCV", "Flask", "MySQL", "React"],
        "category": "AI & Machine Learning",
        "github": "https://github.com/sanjayGL2006/smart-attendance-yolo",
        "icon": "fa-clipboard-user",
        "year": 2026,
        "status": "Completed"
    },
    {
        "id": 125,
        "name": "spvm3-campus-placement",
        "title": "SPVM³ Campus Placement AI Suite",
        "tagline": "AI placement suite with ATS resume scoring & career intelligence.",
        "desc": "AI-powered campus placement & career intelligence suite: automated ATS resume analysis, skills gap roadmaps, safe AI natural language queries, and department analytics.",
        "tech": ["Python", "Flask", "Gemini API", "React", "MySQL", "Tailwind CSS"],
        "category": "Management & Enterprise Systems",
        "github": "https://github.com/sanjayGL2006/spvm3-campus-placement",
        "icon": "fa-user-graduate",
        "year": 2026,
        "status": "Completed"
    },
    {
        "id": 126,
        "name": "spvm3-car-game",
        "title": "SPVM³ 2D Physics Racing Game",
        "tagline": "200-level physics racing game with Web Audio & Python telemetry.",
        "desc": "Action-packed 2D physics racing game featuring 200-level stage progression, 60+ customizable vehicles, multi-layer parallax scenery, real-time audio synthesis, and companion Python server.",
        "tech": ["HTML5 Canvas", "JavaScript", "Python", "Web Audio API", "CSS3"],
        "category": "Games",
        "github": "https://github.com/sanjayGL2006/spvm3-car-game",
        "icon": "fa-car-side",
        "year": 2026,
        "status": "Completed"
    },
    {
        "id": 127,
        "name": "text2img-studio",
        "title": "Text2Img AI Studio",
        "tagline": "Stable Diffusion text-to-image studio with generation history.",
        "desc": "Full-stack Flask web app for AI text-to-image generation powered by Stable Diffusion with built-in MySQL/SQLite generation history tracking.",
        "tech": ["Python", "Flask", "Stable Diffusion API", "MySQL", "HTML5", "CSS3"],
        "category": "AI & Machine Learning",
        "github": "https://github.com/sanjayGL2006/text2img-studio",
        "icon": "fa-wand-magic-sparkles",
        "year": 2026,
        "status": "Completed"
    },
    {
        "id": 128,
        "name": "sanjay-gl-website-carbon-intelligence",
        "title": "Website Carbon Intelligence Auditor",
        "tagline": "Web app & API for auditing website carbon footprint & energy telemetry.",
        "desc": "SANJAY GL Website Carbon Intelligence — A real-time web application and developer API to audit website carbon footprints, HTTP page payload telemetry, energy consumption (SWD v4), and green hosting checks.",
        "tech": ["HTML5", "CSS3", "JavaScript", "Node.js", "SWD v4 API"],
        "category": "Tools, Systems & Utilities",
        "github": "https://github.com/sanjayGL2006/sanjay-gl-website-carbon-intelligence",
        "icon": "fa-leaf",
        "year": 2026,
        "status": "Completed"
    },
    {
        "id": 129,
        "name": "resume-analyzer",
        "title": "AI Resume & Skill Gap Analyzer",
        "tagline": "TF-IDF vector matching for resume ATS scoring against job descriptions.",
        "desc": "AI-powered resume match & skill gap analyzer built with Flask and MySQL. Uses TF-IDF vectorization to score resumes against job descriptions, highlight missing skills, and persist analysis results.",
        "tech": ["Python", "Flask", "Scikit-learn", "TF-IDF", "MySQL", "HTML5"],
        "category": "AI & Machine Learning",
        "github": "https://github.com/sanjayGL2006/resume-analyzer",
        "icon": "fa-file-invoice",
        "year": 2026,
        "status": "Completed"
    },
    {
        "id": 130,
        "name": "image-to-svg-converter",
        "title": "Image to Vector SVG Converter",
        "tagline": "Client-side image to vector SVG converter with Bezier smoothing.",
        "desc": "Blazingly fast, client-side tool to convert JPG, PNG, and WEBP images into clean, scalable SVG vector graphics with K-means color quantization and Bezier curve smoothing.",
        "tech": ["JavaScript", "HTML5 Canvas", "K-Means", "SVG", "CSS3"],
        "category": "Tools, Systems & Utilities",
        "github": "https://github.com/sanjayGL2006/image-to-svg-converter",
        "icon": "fa-vector-square",
        "year": 2026,
        "status": "Completed"
    },
    {
        "id": 131,
        "name": "Paperless-Office-System",
        "title": "Paperless Office Document Workspace",
        "tagline": "Privacy-first digital document workspace with drag & drop storage.",
        "desc": "Paperless Office System is a modern, privacy-first digital document workspace. Eliminate paper waste, organize files with drag-and-drop local storage, and search records in real time.",
        "tech": ["JavaScript", "HTML5", "IndexedDB", "CSS3", "Bootstrap"],
        "category": "Management & Enterprise Systems",
        "github": "https://github.com/sanjayGL2006/Paperless-Office-System",
        "icon": "fa-folder-closed",
        "year": 2026,
        "status": "Completed"
    },
    {
        "id": 132,
        "name": "Traffic-Vehicle-Object-Detection-with-YOLOv8",
        "title": "Traffic & License Plate Detection (YOLOv8)",
        "tagline": "Real-time webcam traffic monitoring & vehicle recognition.",
        "desc": "Real-time object detection web app built with Flask, OpenCV (MobileNet-SSD), and YOLOv8. Features live webcam video streaming, vehicle and license plate recognition, and automated detection logging.",
        "tech": ["Python", "YOLOv8", "OpenCV", "Flask", "MySQL"],
        "category": "AI & Machine Learning",
        "github": "https://github.com/sanjayGL2006/Traffic-Vehicle-Object-Detection-with-YOLOv8",
        "icon": "fa-car",
        "year": 2026,
        "status": "Completed"
    },
    {
        "id": 133,
        "name": "DataGauge-Dataset-Quality-Monitoring-System",
        "title": "DataGauge — Dataset Quality Monitoring",
        "tagline": "Full-stack CSV/Excel quality scoring, issue flags, and PDF reports.",
        "desc": "Full-stack dataset quality monitoring system built with FastAPI, React, and Pandas. Automatically computes 0-100 quality scores, flags data issues, provides guided cleaning, interactive dashboards, and PDF exports.",
        "tech": ["FastAPI", "React", "Pandas", "Python", "JavaScript", "Recharts"],
        "category": "AI & Machine Learning",
        "github": "https://github.com/sanjayGL2006/DataGauge-Dataset-Quality-Monitoring-System",
        "icon": "fa-gauge-high",
        "year": 2026,
        "status": "Completed"
    },
    {
        "id": 134,
        "name": "accident-risk-prediction",
        "title": "Accident Risk Prediction Model",
        "tagline": "Machine Learning based traffic accident risk prediction.",
        "desc": "Machine Learning web application that predicts traffic accident risks using road conditions, weather, traffic volume, and historical accident patterns.",
        "tech": ["Python", "Flask", "Scikit-learn", "Pandas", "SQLite"],
        "category": "AI & Machine Learning",
        "github": "https://github.com/sanjayGL2006/accident-risk-prediction",
        "icon": "fa-triangle-exclamation",
        "year": 2026,
        "status": "Completed"
    },
    {
        "id": 135,
        "name": "daily-task-nexus",
        "title": "Daily Task Nexus",
        "tagline": "Minimalist, locally-persistent task manager with custom animations.",
        "desc": "Minimalist, locally-persistent Daily Task manager built with HTML5, CSS3 (Custom Animations & Gradients), and Vanilla JavaScript featuring dynamic filtering and task lifecycle tracking.",
        "tech": ["HTML5", "CSS3", "JavaScript", "LocalStorage"],
        "category": "Tools, Systems & Utilities",
        "github": "https://github.com/sanjayGL2006/daily-task-nexus",
        "icon": "fa-circle-check",
        "year": 2026,
        "status": "Completed"
    }
]

# Update knowledge.json
with open('d:/portfolio/knowledge.json', 'r', encoding='utf-8') as f:
    knowledge = json.load(f)

k_list = knowledge.get("projects", {}).get("list", [])
existing_titles = {p.get("title", "").lower(): p for p in k_list}

for repo in repos_info:
    title_lower = repo["title"].lower()
    name_lower = repo["name"].lower()
    
    found = False
    for p in k_list:
        p_title = p.get("title", "").lower()
        if title_lower in p_title or name_lower in p_title:
            p["github"] = repo["github"]
            p["description"] = repo["desc"]
            found = True
            break
            
    if not found:
        k_list.append({
            "id": repo["id"],
            "title": repo["title"],
            "category": repo["category"],
            "tagline": repo["tagline"],
            "description": repo["desc"],
            "tech": repo["tech"],
            "github": repo["github"],
            "year": repo["year"],
            "status": "Completed"
        })

knowledge["projects"]["list"] = k_list
knowledge["projects"]["total_count"] = len(k_list)

with open('d:/portfolio/knowledge.json', 'w', encoding='utf-8') as f:
    json.dump(knowledge, f, indent=2)

print(f"Updated knowledge.json! Total projects now in list: {len(k_list)}")
