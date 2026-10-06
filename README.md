# Sanjay G. L. — Full Stack AI Developer Portfolio & Sanjay AIOS v2.5

[![Live Site](https://img.shields.io/badge/Live_Site-sanjaygl30ai.vercel.app-10b981?style=for-the-badge&logo=vercel)](https://sanjaygl30ai.vercel.app/)
[![Python](https://img.shields.io/badge/Backend-Flask_3.0-3776AB?style=for-the-badge&logo=python)](https://flask.palletsprojects.com/)
[![Docker](https://img.shields.io/badge/Container-Docker-2496ED?style=for-the-badge&logo=docker)](https://www.docker.com/)
[![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)](LICENSE)

Official AI-powered developer portfolio, operating system, and interactive technical co-pilot for **Sanjay G. L. (Sanju)** — BCA Student, Full Stack Developer, AI Agent Engineer, and Cybersecurity Explorer from Shivamogga, Karnataka.

---

## 🌟 Key Highlights & Statistical Reality

- **98+ Production & Showcase Projects**: Full-stack web applications, AI agents, e-commerce platforms, security scanners, utilities, and games.
- **222+ Verified Certifications**: Comprehensive credential archive covering Cisco Networking Academy, Oasis Infobyte AICTE Internship, HackerRank Skill Certifications, Microsoft Azure, MeitY AI Ethics, and NPTEL.
- **Sanjay AIOS v2.5 (Deep Learning Edition)**: Neural portfolio co-pilot powered by Gemini API, trained on real datasets, technical interview question bank, and personal project roadmaps.

- **SEO & Digital Identity Optimization**: 100% standardized canonical clean URLs (`sanjaygl30ai.vercel.app`), dynamic project routing (`/projects/<slug>`), Schema.org `Person` and `SoftwareSourceCode` JSON-LD structured data, strict security headers (CSP, HSTS), and `data/identity.json` consolidation for consistent search engine indexing.
- **Next.js SEO Analyzer Dashboard**: Custom built internal React/Tailwind application (`/seo-analyzer`) used to analyze cross-platform personal brand identity, search keyword matches, and profile health.

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
│   ├── projectsData.js      # 98 Projects dataset
│   ├── certificatesData.js  # 222 Certificates dataset
│   ├── home.js              # Home page animations & stats
│   ├── projectsPage.js      # 3D Flip cards & filter logic
│   └── certificatesPage.js  # Gallery grid, timeline & Drive preview modal
├── app.py                   # Flask backend server & Gemini AI endpoint
├── index.html               # Main homepage & interactive OS view
├── projects.html            # Projects showcase page (98+ projects)
├── certificates.html        # Verified credentials page (222+ certificates)
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

2. **Check container status & health**:
   ```bash
   docker ps
   curl http://localhost:5000/health
   ```

3. **Stop containers**:
   ```bash
   docker-compose down
   ```

---

### Option C: Kubernetes Orchestration Deployment (Kustomize)

1. **Deploy all manifests via Kustomize**:
   ```bash
   kubectl apply -k k8s/
   ```

2. **Verify pod status, deployment, storage, and autoscaler**:
   ```bash
   kubectl get all,pvc -n portfolio
   ```

3. **Port forward service for local testing**:
   ```bash
   kubectl port-forward svc/sanjay-portfolio-service 5000:80 -n portfolio
   ```

4. **Tear down deployment**:
   ```bash
   kubectl delete -k k8s/
   ```

---

### Option D: Helm Chart Package Deployment

1. **Install or upgrade release via Helm**:
   ```bash
   helm upgrade --install sanjay-portfolio ./helm/sanjay-portfolio -n portfolio --create-namespace
   ```

2. **Check release status & revision history**:
   ```bash
   helm list -n portfolio
   helm status sanjay-portfolio -n portfolio
   ```

3. **Uninstall Helm release**:
   ```bash
   helm uninstall sanjay-portfolio -n portfolio
   ```

---

### 📬 Postman API Testing Collection & Environment

You can import the pre-configured Postman collection and environment to test all backend endpoints:
1. Open **Postman** -> Click **Import**.
2. Select [`postman/sanjay_aios_portfolio.postman_collection.json`](file:///d:/portfolio/postman/sanjay_aios_portfolio.postman_collection.json).
3. Select [`postman/sanjay_aios_portfolio.postman_environment.json`](file:///d:/portfolio/postman/sanjay_aios_portfolio.postman_environment.json).
4. Set active environment to **Sanjay AIOS Portfolio Environment** and run your requests against `http://localhost:5000` or production!

---

### 📖 Kubernetes Learning Guide
For a step-by-step tutorial on Kubernetes architecture, object definitions, `kubectl` cheatsheet, and learning concepts, see the dedicated [**`k8s/README.md`**](file:///d:/portfolio/k8s/README.md).

---

## 🔗 Key API Endpoints

| Endpoint | Method | Description |
|---|---|---|
| `GET /` | `GET` | Main Portfolio Homepage |
| `GET /health` | `GET` | Health Check Endpoint for Docker & Kubernetes Probes |
| `GET /api/stats` | `GET` | Returns live statistical counters (Projects, Certificates, Visits) |
| `GET /api/projects` | `GET` | Returns JSON dataset of all 98 projects |
| `GET /api/certificates` | `GET` | Returns JSON dataset of all 222 verified certificates |
| `POST /chat` | `POST` | Interacts with Sanjay AIOS v2.5 assistant (`{"message": "..."}`) |
| `POST /api/contact` | `POST` | Submits user contact form messages |

---

## 👨‍💻 Author & Connect & SPVM 3 Tech Solution

**Sanjay G. L. (Sanju)**  
*Full Stack AI Developer & BCA Student*  
- **Portfolio**: [sanjaygl30ai.vercel.app](https://sanjaygl30ai.vercel.app/)  
- **Email**: [sanjaygl2006@gmail.com](mailto:sanjaygl2006@gmail.com)  
- **GitHub**: [@sanjayGL2006](https://github.com/sanjayGL2006)  
- **SPVM 3 Tech Solution - Instagram**: [@spvm3techsolution](https://www.instagram.com/spvm3techsolution)  
- **SPVM 3 Tech Solution - YouTube**: [@spvm3techsolution](https://www.youtube.com/@spvm3techsolution)  
- **Personal LinkedIn**: [sanjay-gl-b86631336](https://www.linkedin.com/in/sanjay-gl-b86631336)
- **SPVM 3 Tech Solution - LinkedIn**: [spvm3-tech-solution](https://www.linkedin.com/company/spvm3-tech-solution)

---

© 2026 Sanjay G. L. Engineered for Performance & Aesthetics.
