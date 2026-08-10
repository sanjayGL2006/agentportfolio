# Sanjay G. L. — Full Stack AI Developer Portfolio & Sanjay AIOS v2.5

[![Live Site](https://img.shields.io/badge/Live_Site-sanjaygl30ai.vercel.app-10b981?style=for-the-badge&logo=vercel)](https://sanjaygl30ai.vercel.app/)
[![Python](https://img.shields.io/badge/Backend-Flask_3.0-3776AB?style=for-the-badge&logo=python)](https://flask.palletsprojects.com/)
[![Supabase](https://img.shields.io/badge/Database-Supabase_pgvector-3ECF8E?style=for-the-badge&logo=supabase)](https://supabase.com/)
[![Docker](https://img.shields.io/badge/Container-Docker-2496ED?style=for-the-badge&logo=docker)](https://www.docker.com/)
[![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)](LICENSE)

Official AI-powered developer portfolio, operating system, and interactive technical co-pilot for **Sanjay G. L. (Sanju)** — BCA Student, Full Stack Developer, AI Agent Engineer, and Cybersecurity Explorer from Shivamogga, Karnataka.

---

## 🌟 Key Highlights & Statistical Reality

- **28+ Production & Showcase Projects**: Full-stack web applications, AI agents, e-commerce platforms, security scanners, utilities, and games.
- **86+ Verified Certifications**: Comprehensive credential archive covering Cisco Networking Academy, Oasis Infobyte AICTE Internship, HackerRank Skill Certifications, Microsoft Azure, MeitY AI Ethics, and NPTEL.
- **Sanjay AIOS v2.5 (Deep Learning Edition)**: Neural portfolio co-pilot powered by Gemini API, trained on real datasets, technical interview question bank, and personal project roadmaps.
- **Supabase Cloud Memory & Continuous Deep Learning**: Integrated Supabase database with `aios_chat_logs` table, Row Level Security (RLS), and `pgvector` embeddings for storing user queries and auto-training the AI co-pilot.
- **SEO & Social Optimization**: 100% standardized canonical URLs (`sanjaygl30ai.vercel.app`), 1200×630px Open Graph PNG social banner, Schema.org `Person` JSON-LD structured data, and `<noscript>` static fallback lists for search engine indexing.

---

## ⚡ Supabase & Deep Learning Architecture

### 1. Database Schema (`supabase_schema.sql`)
```sql
-- Enable vector & uuid extensions for neural embeddings & chat logging
CREATE EXTENSION IF NOT EXISTS vector;
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE IF NOT EXISTS aios_chat_logs (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    session_id VARCHAR(255),
    user_query TEXT NOT NULL,
    agent_response TEXT NOT NULL,
    query_embedding vector(1536),
    created_at TIMESTAMPTZ DEFAULT NOW()
);

ALTER TABLE aios_chat_logs ENABLE ROW LEVEL SECURITY;
```

### 2. Environment Configuration (`.env`)
```env
SUPABASE_URL=https://mglzwnampheswtjzrcbf.supabase.co
SUPABASE_KEY=sb_publishable_vuV_ZmS859v1QUhQHISoqg_nkN-DWFl
SUPABASE_SECRET_KEY=your_supabase_secret_key_here
```

---

## 🚀 Active Technical Roadmaps (Sanjay AIOS v2.5)

### 📌 Immediate Roadmap (Target: November – December 2026)
1. **Web Application Vulnerability Scanner**: Automated security scanner detecting OWASP Top 10, XSS, and SQL Injection vulnerabilities.
2. **AI Face Emotion Detection**: Real-time computer vision deep learning model for classifying facial expressions in video streams.
3. **AI Meeting Notes Generator**: NLP-powered audio transcription and summary generator for key meeting takeaways.
4. **AI Resume Analysis**: Automated resume analyzer evaluating candidate skills, formatting, and role alignment.
5. **AI Coding Agent / Code Editor Agent**: Autonomous programming co-pilot capable of code generation, refactoring, and debugging.
6. **Distributed Chat Application (`chatbot.ai`)**: Low-latency, scalable messaging architecture built with WebSockets and gRPC.

### 📌 Future Roadmap (Target: February – March 2027)
1. **Multi-Language AI Voice Assistant**: Voice assistant optimized for Indian regional languages.
2. **Freelance Service Platform**: Custom 3D web platform offering freelance services (3D web dev, PPT generation, automated notes, and UI design).

---

## 🛠️ Architecture & Tech Stack

- **Frontend**: Vanilla HTML5, CSS3 (Glassmorphic dark design system), JavaScript (ES6+), Three.js 3D background canvas.
- **Backend API**: Python 3.11, Flask WSGI framework, Flask-SQLAlchemy ORM, Gunicorn.
- **AI & ML Integration**: Google Gemini API, PyPDF, OpenCV, Custom Prompt Context Injection.
- **Databases**: SQLite (`portfolio.db`) / MySQL, Google Drive API thumbnail integration.
- **Containerization**: Docker, Docker Compose, multi-stage lightweight builds.

---

## 📁 Repository Structure

```text
portfolio/
├── assets/                  # Logos, favicons, og-banner.png, agent_knowledge.json
├── css/                     # Glassmorphic CSS design system (styles.css)
├── js/                      # Frontend modules & datasets
│   ├── aiAssistant.js       # Sanjay AIOS v2.5 Floating Chat Widget
│   ├── projectsData.js      # 28 Projects dataset
│   ├── certificatesData.js  # 86 Certificates dataset
│   ├── home.js              # Home page animations & stats
│   ├── projectsPage.js      # 3D Flip cards & filter logic
│   └── certificatesPage.js  # Gallery grid, timeline & Drive preview modal
├── app.py                   # Flask backend server & Gemini AI endpoint
├── index.html               # Main homepage & interactive OS view
├── projects.html            # Projects showcase page (28 projects)
├── certificates.html        # Verified credentials page (86 certificates)
├── Dockerfile               # Production Docker container definition
├── docker-compose.yml       # One-command local Docker environment
├── .dockerignore            # Container build exclusions
├── robots.txt               # Web crawler directives
├── sitemap.xml              # Site URL index
└── vercel.json              # Vercel serverless deployment config
```

---

## 💻 Local Quickstart

### Option A: Standard Python Environment

1. **Clone the repository**:
   ```bash
   git clone https://github.com/sanjayGL2006/agentportfolio.git
   cd portfolio
   ```

2. **Create and activate a virtual environment**:
   ```bash
   # Windows (PowerShell)
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1

   # Linux / macOS
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask application**:
   ```bash
   python app.py
   ```

5. **Open in browser**:
   Navigate to `http://localhost:5000`

---

### Option B: Docker Container Deployment

1. **Build and run with Docker Compose**:
   ```bash
   docker-compose up --build -d
   ```

2. **Check container status**:
   ```bash
   docker ps
   ```

3. **Stop containers**:
   ```bash
   docker-compose down
   ```

---

## 🔗 Key API Endpoints

| Endpoint | Method | Description |
|---|---|---|
| `GET /` | `GET` | Main Portfolio Homepage |
| `GET /api/stats` | `GET` | Returns live statistical counters (Projects, Certificates, Visits) |
| `GET /api/projects` | `GET` | Returns JSON dataset of all 28 projects |
| `GET /api/certificates` | `GET` | Returns JSON dataset of all 86 verified certificates |
| `POST /chat` | `POST` | Interacts with Sanjay AIOS v2.5 assistant (`{"message": "..."}`) |
| `POST /api/contact` | `POST` | Submits user contact form messages |

---

## 👨‍💻 Author & Connect

**Sanjay G. L. (Sanju)**  
*Full Stack AI Developer & BCA Student*  
- **Portfolio**: [sanjaygl30ai.vercel.app](https://sanjaygl30ai.vercel.app/)  
- **Email**: [sanjaygl2006@gmail.com](mailto:sanjaygl2006@gmail.com)  
- **GitHub**: [@sanjayGL2006](https://github.com/sanjayGL2006)  
- **LinkedIn**: [linkedin.com/in/sanjaygl3006](https://www.linkedin.com/in/sanjaygl3006/)  
- **Instagram**: [@me__sanjaygl8123](https://www.instagram.com/me__sanjaygl8123)

---

© 2026 Sanjay G. L. Engineered for Performance & Aesthetics.
