// Projects Dataset for Sanjay G. L. Portfolio
// Categorized into 6 main sectors:
// 1. AI & Machine Learning
// 2. Management & Enterprise Systems
// 3. Web Applications & Portals
// 4. Tools, Systems & Utilities
// 5. Games
// 6. Portfolios, Profiles & Tributes

const PROJECTS_DATA = [
  // ===================== 1. AI & MACHINE LEARNING =====================
  {
    id: 29,
    title: "DataGauge — Dataset Quality Monitoring System",
    year: 2026,
    category: "AI & Machine Learning",
    tagline: "Full-stack CSV/Excel quality scoring, issue flags, guided cleaning, and PDF/Excel reports.",
    desc: "A FastAPI + React dataset quality platform that uploads CSV/Excel files and computes a live 0–100 quality score, categorized issues, interactive dashboards, guided cleaning, and downloadable PDF/Excel reports.",
    tech: ["Python", "FastAPI", "Pandas", "NumPy", "SciPy", "SQLAlchemy", "React", "Vite", "Tailwind CSS", "Recharts", "JWT", "ReportLab", "OpenPyXL"],
    live: "https://sanjaygl2006.vercel.app/",
    github: "https://github.com/sanjayGL2006/DataGauge-Dataset-Quality-Monitoring-System",
    status: "Completed",
    featured: true,
    icon: "fa-gauge-high",
    image: "assets/datagauge_cover.svg",
    overview: "DataGauge lets users upload CSV or Excel datasets and receive an automatic quality assessment: completeness, validity, consistency, uniqueness, and anomaly scores plus issue management, history trends, and user-approved cleaning that never mutates the original file.",
    architecture: "React 18 (Vite, Tailwind, Axios, Recharts) talks to a FastAPI backend. Pandas/NumPy/SciPy power a modular quality engine (one module per check). SQLAlchemy stores users, datasets, issues, and history with PostgreSQL, MySQL, or SQLite via DATABASE_URL. JWT + bcrypt protect routes; ReportLab and OpenPyXL generate reports.",
    features: [
      "JWT authentication with Admin / Analyst / Viewer roles",
      "Drag-and-drop CSV, XLSX, and XLS upload with validation pipeline",
      "Modular quality engine: completeness, duplicates, types, validity, consistency, dates, booleans, outliers, logical rules",
      "Configurable 0–100 weighted quality score (defaults: 25/20/20/20/15)",
      "Interactive dashboard with 10 Recharts visualizations",
      "Searchable preview with problematic-cell highlighting",
      "Issue workflow: Open → Reviewed → Resolved / Ignored",
      "Guided cleaning that writes a new file and compares before/after scores",
      "PDF, Excel, and CSV issue reports",
      "Quality history trends across analysis runs"
    ],
    stats: {
      "Quality Score": "0–100 live",
      "Check Modules": "10+",
      "Chart Types": "10",
      "Reports": "PDF + Excel"
    }
  },
  {
    id: 27,
    title: "DermAI — AI-Powered Skincare Diagnosis App",
    year: 2026,
    category: "AI & Machine Learning",
    tagline: "Deep learning skin lesion analysis and dermatology diagnostic assistant.",
    desc: "An AI-powered dermatological diagnostic assistant that screens skin lesions using CNN models, providing risk classifications and clinical care recommendations.",
    tech: ["Python", "Flask", "TensorFlow", "Keras", "OpenCV", "Scikit-image", "HTML5", "CSS3", "JavaScript"],
    live: "https://sanjaygl2006.vercel.app/",
    github: "https://github.com/sanjayGL2006/DermAI-AI-Powered-Skincare-Diagnosis-App",
    status: "Completed",
    featured: true,
    icon: "fa-stethoscope",
    image: "assets/dermait_cover.png",
    overview: "DermAI is a healthcare AI utility applying Deep Learning Convolutional Neural Networks (CNN) to screen and classify skin lesions from digital camera images. It serves as a triage assistant for clinical dermatology workflows.",
    architecture: "Developed on a Python Flask framework serving predictions from a TensorFlow/Keras model. The frontend handles image uploads, local preprocessing via HTML5 Canvas, and displays prediction graphs and probabilities using Chart.js.",
    features: [
      "TensorFlow / Keras CNN Model (94% accuracy)",
      "Image preprocessing pipeline using OpenCV & Scikit-image",
      "Real-time chart display of prediction probabilities",
      "Dermatology triage flow charts & clinical advice recommendations",
      "Secure user upload data sanitization",
      "Mobile-first responsive design for quick triage tests",
      "PDF diagnostic summary generation"
    ],
    stats: {
      "Model Accuracy": "94%",
      "Training Epochs": "75 Epochs",
      "Inference Time": "< 120ms"
    }
  },
  {
    id: 24,
    title: "Accident Risk Prediction",
    year: 2026,
    category: "AI & Machine Learning",
    tagline: "Machine Learning based accident risk prediction system for safer roads.",
    desc: "A Machine Learning web application that predicts traffic accident risks using road conditions, weather, traffic volume, and historical accident patterns.",
    tech: ["HTML5", "CSS3", "JavaScript", "Python", "Flask", "Scikit-learn", "Pandas", "NumPy", "Joblib", "SQLite"],
    live: "https://sanjaygl2006.vercel.app/",
    github: "https://github.com/sanjayGL2006/accident-risk-prediction",
    status: "Completed",
    featured: true,
    icon: "fa-triangle-exclamation",
    image: "assets/accident_prediction_cover.png",
    overview: "A Machine Learning web application that predicts traffic accident risks using road conditions, weather, traffic volume, and historical accident patterns to improve road safety.",
    architecture: "Python Flask application utilizing a pre-trained Random Forest Classifier model saved via Joblib. The frontend collects road parameters and environmental factors, sending asynchronous REST requests to Flask endpoints for real-time risk probability calculation.",
    features: [
      "Random Forest Machine Learning model achieving 98% prediction accuracy",
      "Multi-variable input parameters: Weather conditions, Road surface, Traffic volume, Lighting",
      "Real-time hazard level scoring and percentage risk index output",
      "SQLite integration storing historical accident trends and road safety data",
      "Interactive data visualizations for high-risk zones and recommended speed safety margins"
    ],
    timeline: [
      "Dataset aggregation & exploratory data analysis using Pandas and NumPy",
      "Feature engineering & Random Forest classifier training with Scikit-learn",
      "Flask REST API backend development & SQLite database schema design",
      "Responsive web interface build with real-time risk calculation dashboard"
    ],
    structure: [
      "app.py — Flask web application & API route handlers",
      "model/ — Pre-trained Random Forest ML model (joblib) & scaler",
      "static/ & templates/ — Interactive calculator UI & CSS/JS assets",
      "database/ — SQLite storage for historical traffic accident logs"
    ],
    futureScope: [
      "Integration with live weather forecasting APIs and GPS mapping",
      "Deep Learning (LSTM) temporal accident risk forecasting",
      "Driver mobile push alert notifications for high-risk road zones"
    ],
    stats: {
      "Accuracy": "98%",
      "Dataset Size": "10k+ Records",
      "Model Type": "Random Forest"
    }
  },
  {
    id: 1,
    title: "AI Agent using Google API",
    year: 2025,
    category: "AI & Machine Learning",
    tagline: "Autonomous assistant powered by Google AI APIs for intelligent conversations & task automation.",
    desc: "An AI-powered assistant integrated with Google AI APIs for intelligent conversations, reasoning, and context-aware task automation.",
    tech: ["Python", "HTML5", "CSS3", "JavaScript", "Google AI API", "Google Cloud Run"],
    live: "https://sanjaygl2006.vercel.app/",
    github: "https://github.com/sanjayGL2006/AI-Agent-used-google-api",
    status: "Completed",
    featured: true,
    icon: "fa-robot",
    stats: {
      "API": "Google AI Studio",
      "Mode": "Autonomous Agent",
      "Deployment": "Cloud Run"
    }
  },
  {
    id: 26,
    title: "Sindhanai Full Stack AI",
    year: 2026,
    category: "AI & Machine Learning",
    tagline: "Full stack AI-driven content generation and workflow platform.",
    desc: "A premium full-stack AI workspace facilitating document summarization, customized coding templates, automated content creation, and secure chatbot dialogs.",
    tech: ["React", "Node.js", "Express", "MongoDB", "Google Gemini API", "Tailwind CSS", "JWT"],
    live: "https://sanjaygl2006.vercel.app/",
    github: "https://github.com/sanjayGL2006/sindhanai-fullstack-ai",
    status: "Completed",
    featured: true,
    icon: "fa-brain",
    image: "assets/sindhanai_cover.png",
    stats: {
      "API Latency": "< 800ms",
      "Accuracy": "Gemini Pro",
      "Auth Model": "JWT Token"
    }
  },
  {
    id: 25,
    title: "Sai AI Assistant",
    year: 2026,
    category: "AI & Machine Learning",
    tagline: "Modern AI assistant powered by Gemini with productivity tools.",
    desc: "An AI-powered assistant capable of chatting, answering educational questions, generating code, showing live news, saving conversations, and helping users with productivity.",
    tech: ["HTML", "CSS", "JavaScript", "Python", "Flask", "SQLite", "Google Gemini API"],
    live: "https://sanjaygl2006.vercel.app/",
    github: "https://github.com/sanjayGL2006/sai_assistant",
    status: "Completed",
    featured: true,
    icon: "fa-robot",
    image: "assets/sai_assistant_cover.png",
    stats: {
      "API Version": "Gemini Pro",
      "Response Time": "< 1.5s",
      "Storage": "SQLite DB"
    }
  },
  {
    id: 30,
    title: "Traffic & Vehicle Object Detection with YOLOv8",
    year: 2026,
    category: "AI & Machine Learning",
    tagline: "Real-time computer vision system for traffic monitoring & vehicle detection using YOLOv8.",
    desc: "High-performance object detection model trained on traffic surveillance datasets to detect cars, buses, motorcycles, and pedestrians with bounding box confidence scores.",
    tech: ["Python", "YOLOv8", "OpenCV", "PyTorch", "Flask", "Chart.js"],
    live: "https://sanjaygl2006.vercel.app/",
    github: "https://github.com/sanjayGL2006/Traffic-Vehicle-Object-Detection-with-YOLOv8",
    status: "Completed",
    featured: false,
    icon: "fa-car-side",
    overview: "Computer vision application that processes live camera feeds or video files, detecting vehicle classes, counting traffic density, and calculating road congestion stats.",
    stats: {
      "Model": "YOLOv8 Nano/Small",
      "Detection Speed": "69+ FPS",
      "Precision": "92% mAP"
    }
  },
  {
    id: 37,
    title: "Indian Traffic Sign Detection App",
    year: 2026,
    category: "AI & Machine Learning",
    tagline: "Deep learning traffic sign classification for Indian road navigation & autonomous safety.",
    desc: "Computer vision app trained to recognize Indian regulatory, warning, and informatory traffic road signs in real-time from camera feeds.",
    tech: ["Python", "TensorFlow", "Keras", "OpenCV", "Flask"],
    live: "https://sanjaygl2006.vercel.app/",
    github: "https://github.com/sanjayGL2006/indian-traffic-sign-detection",
    status: "Completed",
    featured: false,
    icon: "fa-diamond-turn-right",
    stats: {
      "Categories": "58 Sign Classes",
      "Accuracy": "95%",
      "Framework": "Keras CNN"
    }
  },
  {
    id: 38,
    title: "Smart Spam Email & SMS Detector",
    year: 2026,
    category: "AI & Machine Learning",
    tagline: "NLP Naive Bayes & Logistic Regression text classification for spam detection.",
    desc: "Machine Learning model application that analyzes email text and SMS messages to accurately flag spam, phishing, and scam messages.",
    tech: ["Python", "Scikit-learn", "NLTK", "Flask", "HTML5/CSS3"],
    live: "https://sanjaygl2006.vercel.app/",
    github: "https://github.com/sanjayGL2006/smart-spam-detector",
    status: "Completed",
    featured: false,
    icon: "fa-shield-cat",
    stats: {
      "Model": "Multinomial Naive Bayes",
      "Accuracy": "97.8%",
      "Dataset": "SMS Spam Collection"
    }
  },
  {
    id: 18,
    title: "Surya Chatbot",
    year: 2025,
    category: "AI & Machine Learning",
    tagline: "Interactive conversational AI bot with custom response logic and floating UI.",
    desc: "Rule-based and generative AI chatbot designed to answer queries with an intuitive floating chat window interface and quick answer shortcuts.",
    tech: ["HTML5", "CSS3", "JavaScript", "NLP Rules"],
    live: "https://sanjaygl2006.vercel.app/",
    github: "https://github.com/sanjayGL2006/Surya-chatbot",
    status: "Completed",
    featured: false,
    icon: "fa-comments",
    stats: {
      "Interface": "Floating Widget",
      "Response Time": "< 100ms",
      "Engine": "NLP Dictionary"
    }
  },
  {
    id: 8,
    title: "Kai Assistant",
    year: 2025,
    category: "AI & Machine Learning",
    tagline: "In-browser conversational AI assistant built for instant answers & quick text generation.",
    desc: "Lightweight browser-based virtual assistant capable of quick question answering, task prompts, context formatting, and contextual text generation.",
    tech: ["HTML5", "CSS3", "JavaScript", "AI API"],
    live: "https://sanjaygl2006.vercel.app/",
    github: "https://github.com/sanjayGL2006/kai-assistant",
    status: "Completed",
    featured: false,
    icon: "fa-brain",
    stats: {
      "Type": "Browser Agent",
      "Latency": "Instant",
      "Tech": "JS + AI API"
    }
  },
  {
    id: 31,
    title: "AIML Course & Practical Labs",
    year: 2025,
    category: "AI & Machine Learning",
    tagline: "Comprehensive repository of Artificial Intelligence & Machine Learning practical experiments.",
    desc: "A curated lab notebook containing practical implementations of supervised/unsupervised learning algorithms, neural network architectures, data preprocessing, and model evaluations.",
    tech: ["Python", "Jupyter Notebook", "Scikit-learn", "TensorFlow", "Pandas", "Matplotlib"],
    live: "https://sanjaygl2006.vercel.app/",
    github: "https://github.com/sanjayGL2006/AIML-course-and-Practical",
    status: "Completed",
    featured: false,
    icon: "fa-graduation-cap",
    stats: {
      "Labs": "20+ Notebooks",
      "Algorithms": "Linear/Logistic, SVM, Decision Trees, CNN",
      "Language": "Python"
    }
  },

  // ===================== 2. MANAGEMENT & ENTERPRISE SYSTEMS =====================
  {
    id: 28,
    title: "Paperless Office & Billing Management System",
    year: 2025,
    category: "Management & Enterprise Systems",
    tagline: "Enterprise paperless document workflow, billing & invoice generator.",
    desc: "A professional billing and document management system designed for digital offices and retail storefronts, supporting inventory tracking, tax calculations, and instant PDF invoice generation.",
    tech: ["HTML5", "CSS3", "JavaScript", "SQLite", "Node.js", "Electron.js", "PDFKit"],
    live: "https://sanjaygl2006.vercel.app/",
    github: "https://github.com/sanjayGL2006/Paperless-Office-System",
    status: "Completed",
    featured: true,
    icon: "fa-file-invoice-dollar",
    image: "assets/billing_system_cover.png",
    stats: {
      "DB Model": "SQLite",
      "Export": "PDF Document",
      "Engine": "Node / Electron"
    }
  },
  {
    id: 12,
    title: "Property Manager Dashboard",
    year: 2025,
    category: "Management & Enterprise Systems",
    tagline: "Admin dashboard for real-estate property listings & tenant management.",
    desc: "Administrative web dashboard featuring analytics charts, tenant rent status, maintenance ticket tracking, and property unit occupancy management.",
    tech: ["TypeScript", "React", "Tailwind CSS", "Recharts"],
    live: "https://sanjaygl2006.vercel.app/",
    github: "https://github.com/sanjayGL2006/prop-manager-dash-95721",
    status: "Completed",
    featured: false,
    icon: "fa-chart-line",
    stats: {
      "UI Stack": "React + TypeScript",
      "Styling": "Tailwind CSS",
      "Type": "Real Estate Dashboard"
    }
  },
  {
    id: 39,
    title: "Hospital Management System",
    year: 2025,
    category: "Management & Enterprise Systems",
    tagline: "Comprehensive healthcare portal for patient records, doctor appointments & billing.",
    desc: "Full-stack hospital database system managing patient registrations, doctor schedules, pharmacy billing, and medical department inventory.",
    tech: ["Python", "Flask", "SQLite", "HTML5", "Bootstrap"],
    live: "https://sanjaygl2006.vercel.app/",
    github: "https://github.com/sanjayGL2006/hospital-management-system",
    status: "Completed",
    featured: false,
    icon: "fa-hospital",
    stats: {
      "Modules": "Patient, Doctor, Pharmacy",
      "Database": "SQLite DB",
      "Role": "Enterprise Portal"
    }
  },
  {
    id: 40,
    title: "Student Attendance Management System",
    year: 2025,
    category: "Management & Enterprise Systems",
    tagline: "Automated student attendance tracking & percentage generator.",
    desc: "Desktop/Web application providing class-wise attendance marking, shortage warnings, automated monthly percentage calculation, and CSV record exports.",
    tech: ["Python", "Tkinter", "SQLite", "Pandas"],
    live: "https://sanjaygl2006.vercel.app/",
    github: "https://github.com/sanjayGL2006/attendance_system",
    status: "Completed",
    featured: false,
    icon: "fa-clipboard-user",
    stats: {
      "Features": "Shortage Alerts + Export",
      "Database": "SQLite",
      "Target": "Academic Institutions"
    }
  },
  {
    id: 41,
    title: "Placement Pro Portal",
    year: 2025,
    category: "Management & Enterprise Systems",
    tagline: "College placement cell management portal for student profiles & recruiter drives.",
    desc: "Web portal streamlining campus placement drives, company registrations, student resume submissions, and interview schedule tracking.",
    tech: ["HTML5", "CSS3", "JavaScript", "PHP", "MySQL"],
    live: "https://sanjaygl2006.vercel.app/",
    github: "https://github.com/sanjayGL2006/placement-pro",
    status: "Completed",
    featured: false,
    icon: "fa-user-tie",
    stats: {
      "Stack": "PHP + MySQL",
      "Users": "Students & Recruiters",
      "Feature": "Drive Management"
    }
  },

  // ===================== 3. WEB APPLICATIONS & PORTALS =====================
  {
    id: 13,
    title: "Pure Weaves E-Commerce",
    year: 2025,
    category: "Web Applications & Portals",
    tagline: "Handcrafted saree store with live inventory and inquiry backend.",
    desc: "Elegant e-commerce storefront for artisanal sarees featuring high-definition galleries, dynamic product filters, shopping cart, and Google Sheets serverless database order processing.",
    tech: ["HTML5", "CSS3", "JavaScript", "Google Apps Script", "Vercel"],
    live: "https://pureweaves.vercel.app/",
    github: "https://github.com/sanjayGL2006/pure-weaves-ecommerce",
    status: "Completed",
    featured: true,
    icon: "fa-bag-shopping",
    stats: {
      "Storefront": "Responsive E-Commerce",
      "Database": "Google Sheets API",
      "Deployment": "Vercel"
    }
  },
  {
    id: 5,
    title: "Daily Task Nexus (Grab Notes)",
    year: 2025,
    category: "Web Applications & Portals",
    tagline: "Smart task manager & note-taking application for productive workflows.",
    desc: "Clean productivity suite with quick tag filtering, search indexing, auto-save drafts, task priority checklists, and rich Markdown text rendering.",
    tech: ["TypeScript", "React", "Tailwind CSS", "LocalStorage"],
    live: "https://sanjaygl2006.vercel.app/",
    github: "https://github.com/sanjayGL2006/daily-task-nexus",
    status: "Completed",
    featured: true,
    icon: "fa-note-sticky",
    stats: {
      "Stack": "React + TypeScript",
      "Persistence": "Local Cache",
      "Live App": "Base44"
    }
  },
  {
    id: 4,
    title: "RupeeTrack — Expense Tracker",
    year: 2025,
    category: "Web Applications & Portals",
    tagline: "Comprehensive personal finance & expense tracking web application.",
    desc: "Modern expense tracker enabling users to log transactions, classify income/expenses, monitor monthly budgets, and analyze spending habits with interactive charts.",
    tech: ["HTML5", "CSS3", "JavaScript", "LocalStorage", "Chart.js"],
    live: "https://rupeetrack-app.netlify.app/",
    github: "https://github.com/sanjayGL2006/expense-tracker",
    status: "Completed",
    featured: true,
    icon: "fa-wallet",
    stats: {
      "Category": "Personal Finance",
      "Analytics": "Chart.js",
      "Deployment": "Netlify"
    }
  },
  {
    id: 11,
    title: "Pizza Shop Website",
    year: 2025,
    category: "Web Applications & Portals",
    tagline: "Mouth-watering pizza restaurant website with online order preview.",
    desc: "Dynamic web application for an artisanal pizzeria featuring interactive menu selection, custom pizza builder preview, cart state, and delivery zone checker.",
    tech: ["HTML5", "CSS3", "JavaScript"],
    live: "https://sanjaygl2006.vercel.app/",
    github: "https://github.com/sanjayGL2006/pizza-shop-website",
    status: "Completed",
    featured: false,
    icon: "fa-pizza-slice",
    stats: {
      "UX Design": "Interactive Menu",
      "Cart": "Client JS",
      "Responsive": "Mobile-First"
    }
  },
  {
    id: 22,
    title: "VPN Service Landing Page",
    year: 2025,
    category: "Web Applications & Portals",
    tagline: "High-converting cybersecurity VPN subscription product landing page.",
    desc: "Commercial product landing page presenting VPN feature matrices, pricing tiers, server location maps, speed benchmarks, and security FAQs.",
    tech: ["HTML5", "CSS3", "JavaScript"],
    live: "https://sanjaygl2006.vercel.app/",
    github: "https://github.com/sanjayGL2006/vpn-landing-page1",
    status: "Completed",
    featured: false,
    icon: "fa-key",
    stats: {
      "Design": "Modern Dark Glass UI",
      "Sections": "6 Interactive Blocks",
      "Responsiveness": "100%"
    }
  },
  {
    id: 14,
    title: "Registration Form",
    year: 2025,
    category: "Web Applications & Portals",
    tagline: "Clean modern user registration form with real-time CSS & JS validation.",
    desc: "Interactive registration form featuring real-time input validation, password strength meter, confirmation matching, and polished micro-animations.",
    tech: ["HTML5", "CSS3", "JavaScript"],
    live: "https://sanjaygl2006.vercel.app/",
    github: "https://github.com/sanjayGL2006/Registration-form",
    status: "Completed",
    featured: false,
    icon: "fa-id-card",
    stats: {
      "Validation": "Real-time regex",
      "UI Polish": "Glassmorphism",
      "Lightweight": "Zero Dependencies"
    }
  },
  {
    id: 42,
    title: "Custom Business Website",
    year: 2025,
    category: "Web Applications & Portals",
    tagline: "Modern responsive commercial business website template.",
    desc: "Clean business web template tailored for local agencies and services, featuring hero sliders, service showcases, customer testimonials, and contact forms.",
    tech: ["HTML5", "CSS3", "JavaScript"],
    live: "https://sanjaygl2006.vercel.app/",
    github: "https://github.com/sanjayGL2006/custom-business-website",
    status: "Completed",
    featured: false,
    icon: "fa-briefcase",
    stats: {
      "Layout": "Responsive Business Template",
      "Speed": "Instant",
      "SEO": "Optimized Markup"
    }
  },

  // ===================== 4. TOOLS, SYSTEMS & UTILITIES =====================
  {
    id: 21,
    title: "Vault Secure Auth",
    year: 2025,
    category: "Tools, Systems & Utilities",
    tagline: "Secure authentication portal with password security audits & login UI validation.",
    desc: "Modern security portal UI implementing client-side input validation, password visibility toggles, hash calculation previews, and multi-step authentication layouts.",
    tech: ["HTML5", "CSS3", "JavaScript", "CryptoJS"],
    live: "https://sanjaygl2006.vercel.app/",
    github: "https://github.com/sanjayGL2006/vault-secure-auth",
    status: "Completed",
    featured: false,
    icon: "fa-lock",
    stats: {
      "Security": "Client Hashing",
      "Validation": "Interactive UI",
      "Type": "Auth Portal"
    }
  },
  {
    id: 23,
    title: "Web Calculator JS",
    year: 2025,
    category: "Tools, Systems & Utilities",
    tagline: "Feature-rich web calculator with percentage, square root, and keyboard shortcuts.",
    desc: "Scientific-lite web calculator offering memory recall, percentage formulas, square root functions, calculation history, and physical keypress bindings.",
    tech: ["HTML5", "CSS3", "JavaScript"],
    live: "https://sanjaygl2006.vercel.app/",
    github: "https://github.com/sanjayGL2006/web-calculator-js",
    status: "Completed",
    featured: false,
    icon: "fa-square-root-variable",
    stats: {
      "Functions": "Standard + Scientific",
      "Input": "Touch + Keyboard",
      "History": "Saved per session"
    }
  },
  {
    id: 19,
    title: "Temperature Converter Web App",
    year: 2025,
    category: "Tools, Systems & Utilities",
    tagline: "Instant Celsius, Fahrenheit, and Kelvin scale conversion utility.",
    desc: "Sleek conversion calculator handling instant bi-directional transformations between Celsius, Fahrenheit, and Kelvin temperature scales with visual warmth indicators.",
    tech: ["HTML5", "CSS3", "JavaScript"],
    live: "https://sanjaygl2006.vercel.app/",
    github: "https://github.com/sanjayGL2006/ttemp-convert-web-app",
    status: "Completed",
    featured: false,
    icon: "fa-temperature-high",
    stats: {
      "Scales": "Celsius / Fahrenheit / Kelvin",
      "Conversion": "Real-time input",
      "UI": "Dynamic Gradient"
    }
  },
  {
    id: 2,
    title: "BMI Calculator",
    year: 2025,
    category: "Tools, Systems & Utilities",
    tagline: "Instant health index calculator for height and weight measurements.",
    desc: "Responsive Body Mass Index (BMI) calculator providing immediate health index feedback, target weight ranges, and interactive health gauge visualizations.",
    tech: ["HTML5", "CSS3", "JavaScript"],
    live: "https://sanjaygl2006.vercel.app/",
    github: "https://github.com/sanjayGL2006/bmi_calculator",
    status: "Completed",
    featured: false,
    icon: "fa-calculator",
    stats: {
      "Formula": "Standard BMI",
      "Feedback": "Categorized health status",
      "Speed": "Instant"
    }
  },
  {
    id: 32,
    title: "Bluetooth Chat Utility",
    year: 2025,
    category: "Tools, Systems & Utilities",
    tagline: "Wireless peer-to-peer local messaging app over Bluetooth connections.",
    desc: "Utility application designed to establish direct device-to-device Bluetooth socket connections for offline text messaging and file transfer without internet access.",
    tech: ["Android", "Java", "Bluetooth RFCOMM", "XML"],
    live: "https://sanjaygl2006.vercel.app/",
    github: "https://github.com/sanjayGL2006/bluetooth-chat-",
    status: "Completed",
    featured: false,
    icon: "fa-bluetooth-b",
    stats: {
      "Connection": "RFCOMM Sockets",
      "Mode": "Offline Peer-to-Peer",
      "Platform": "Android / Java"
    }
  },
  {
    id: 33,
    title: "Pixel Perfect Design Tool",
    year: 2025,
    category: "Tools, Systems & Utilities",
    tagline: "Precision screen measurement and grid overlay tool for UI developers.",
    desc: "Developer utility allowing web designers to overlay alignment grids, inspect exact element dimensions in pixels, and verify responsive design fidelity.",
    tech: ["JavaScript", "HTML5 Canvas", "CSS3"],
    live: "https://sanjaygl2006.vercel.app/",
    github: "https://github.com/sanjayGL2006/pixel-perfect",
    status: "Completed",
    featured: false,
    icon: "fa-crop-simple",
    stats: {
      "Precision": "1px grid step",
      "Mode": "Developer Overlay",
      "Tech": "Vanilla JS"
    }
  },
  {
    id: 43,
    title: "Peacock OS — Web Desktop System",
    year: 2025,
    category: "Tools, Systems & Utilities",
    tagline: "Browser-based desktop operating system interface with draggable windows.",
    desc: "Web OS environment mimicking desktop window managers, featuring draggable app windows, file system preview, taskbar, and embedded utilities.",
    tech: ["HTML5", "CSS3", "JavaScript"],
    live: "https://sanjaygl2006.vercel.app/",
    github: "https://github.com/sanjayGL2006/Peacock-OS",
    status: "Completed",
    featured: false,
    icon: "fa-desktop",
    stats: {
      "UI": "Web OS Desktop",
      "Features": "Draggable Windows",
      "Engine": "Vanilla JS"
    }
  },
  {
    id: 44,
    title: "CodeForge — Online Code Editor",
    year: 2025,
    category: "Tools, Systems & Utilities",
    tagline: "In-browser live HTML/CSS/JS code playground and instant previewer.",
    desc: "Lightweight front-end web playground allowing real-time code editing, live preview iframe execution, and syntax highlighting.",
    tech: ["HTML5", "CSS3", "JavaScript"],
    live: "https://sanjaygl2006.vercel.app/",
    github: "https://github.com/sanjayGL2006/codeforge",
    status: "Completed",
    featured: false,
    icon: "fa-code",
    stats: {
      "Preview": "Instant iframe render",
      "Languages": "HTML, CSS, JS",
      "Mode": "Live Playground"
    }
  },

  // ===================== 5. GAMES =====================
  {
    id: 34,
    title: "Chess Game Engine",
    year: 2025,
    category: "Games",
    tagline: "Interactive 2-player chess game with legal move validation and visual board.",
    desc: "A fully functional chess game featuring piece movement rules, castling, en passant checks, move history, and checkmate detection.",
    tech: ["JavaScript", "HTML5", "CSS3", "Chess Logic"],
    live: "https://sanjaygl2006.vercel.app/",
    github: "https://github.com/sanjayGL2006/chess-game",
    status: "Completed",
    featured: true,
    icon: "fa-chess",
    stats: {
      "Logic": "FIDE Move Rules",
      "Players": "2 Players / Local",
      "UI": "Custom Drag & Drop Board"
    }
  },
  {
    id: 20,
    title: "Tic-Tac-Toe Game in Python",
    year: 2025,
    category: "Games",
    tagline: "Classic terminal and graphical Tic-Tac-Toe game in Python.",
    desc: "Console and Tkinter application written in Python demonstrating game matrix evaluation, AI minimax opponent, and turn state management.",
    tech: ["Python", "Tkinter"],
    live: "https://sanjaygl2006.vercel.app/",
    github: "https://github.com/sanjayGL2006/Tic-Tac-Toe-Game-in-python-coder",
    status: "Completed",
    featured: false,
    icon: "fa-brands fa-python",
    stats: {
      "Language": "Python 3",
      "Opponent": "Local 2-Player & Minimax AI",
      "UI": "Terminal & GUI"
    }
  },
  {
    id: 3,
    title: "Digital Board Duel",
    year: 2025,
    category: "Games",
    tagline: "Interactive two-player digital board game with real-time turns & smooth UI.",
    desc: "Modern digital board game featuring glassmorphic graphics, sound synthesizers, turn animations, score tracking, and smooth interactive gameplay.",
    tech: ["TypeScript", "React", "CSS3", "Tailwind CSS"],
    live: "https://sanjaygl2006.vercel.app/",
    github: "https://github.com/sanjayGL2006/digital-board-duel",
    status: "Completed",
    featured: true,
    icon: "fa-gamepad",
    stats: {
      "Framework": "React + TypeScript",
      "Styling": "Tailwind CSS",
      "Live App": "Lovable AI"
    }
  },

  // ===================== 6. PORTFOLIOS, PROFILES & TRIBUTES =====================
  {
    id: 16,
    title: "Sanju Portfolio Pro Hub",
    year: 2025,
    category: "Portfolios, Profiles & Tributes",
    tagline: "Advanced React-powered portfolio with glassmorphism & dynamic transitions.",
    desc: "React portfolio hub engineered with ambient background particle effects, glassmorphic cards, search indexes, and project showcase filters.",
    tech: ["TypeScript", "React", "Tailwind CSS"],
    live: "https://sanjaygl2006.vercel.app/",
    github: "https://github.com/sanjayGL2006/agentportfolio",
    status: "Completed",
    featured: true,
    icon: "fa-laptop-code",
    stats: {
      "Tech": "React + TypeScript",
      "Design": "Glassmorphism",
      "Deployment": "Base44"
    }
  },
  {
    id: 15,
    title: "Sanjay GL Developer Portfolio & Profile",
    year: 2025,
    category: "Portfolios, Profiles & Tributes",
    tagline: "Personal portfolio & developer hub showcasing projects, skills, and credentials.",
    desc: "Responsive developer website featuring 3D ambient space background, terminal command palette, verified certificates archive, AI co-pilot, and contact form.",
    tech: ["HTML5", "CSS3", "JavaScript", "Python", "Flask"],
    live: "https://sanjaygl2006.vercel.app/",
    github: "https://github.com/sanjayGL2006/sanjayGL2006",
    status: "Completed",
    featured: true,
    icon: "fa-globe",
    stats: {
      "Projects": "69+ Cataloged",
      "Certificates": "87+ Verified",
      "AI OS": "Gemini Integration"
    }
  },
  {
    id: 35,
    title: "Sri Mariyamma Temple Portal",
    year: 2025,
    category: "Portfolios, Profiles & Tributes",
    tagline: "Community temple cultural website & event information portal.",
    desc: "Dedicated cultural web portal created to showcase temple history, annual festival schedules, photo galleries, and community announcements.",
    tech: ["HTML5", "CSS3", "JavaScript"],
    live: "https://sanjaygl2006.vercel.app/",
    github: "https://github.com/sanjayGL2006/srimariyammatemple",
    status: "Completed",
    featured: false,
    icon: "fa-place-of-worship",
    stats: {
      "Purpose": "Community & Cultural Portal",
      "Gallery": "High-Res Photography",
      "Language": "Kannada & English"
    }
  },
  {
    id: 36,
    title: "Maya Angelou Tribute Showcase",
    year: 2025,
    category: "Portfolios, Profiles & Tributes",
    tagline: "Literary tribute page celebrating Maya Angelou's poetry, life, and legacy.",
    desc: "Polished biographical tribute webpage highlighting Maya Angelou's famous poems, civil rights contributions, audio recitations, and timeline milestones.",
    tech: ["HTML5", "CSS3", "JavaScript"],
    live: "https://sanjaygl2006.vercel.app/",
    github: "https://github.com/sanjayGL2006/maya-angelou-tribute",
    status: "Completed",
    featured: false,
    icon: "fa-feather-pointed",
    stats: {
      "Subject": "Maya Angelou Tribute",
      "Design": "Classic Editorial Layout",
      "Features": "Poetry Carousel & Quotes"
    }
  }
  ,{
    id: 100,
    title: "Spvm3 Chat",
    year: 2026,
    category: "Web Applications & Portals",
    tagline: "spvm3-chat",
    desc: "SPVM3 Chat: A high-performance real-time chat app featuring instant messaging, multiple chat rooms, typing indicators, and live user presence. Powered by native WebSockets with a FastAPI backend an…",
    tech: ["Python", "FastAPI", "React"],
    live: "https://sanjaygl2006.vercel.app/",
    github: "https://github.com/sanjayGL2006/spvm3-chat",
    status: "Completed",
    featured: false,
    icon: "fa-globe",
    stats: {
      "Type": "GitHub Project",
      "Source": "Auto-imported"
    }
  }
  ,{
    id: 101,
    title: "Social Analytics Ui",
    year: 2026,
    category: "Management & Enterprise Systems",
    tagline: "social-analytics-ui",
    desc: "PulseBoard: A modern social media analytics dashboard built with React, FastAPI, and Recharts. Features follower growth tracking, engagement metrics, and a recent posts feed.",
    tech: ["Python", "FastAPI", "React"],
    live: "https://sanjaygl2006.vercel.app/",
    github: "https://github.com/sanjayGL2006/social-analytics-ui",
    status: "Completed",
    featured: false,
    icon: "fa-chart-line",
    stats: {
      "Type": "GitHub Project",
      "Source": "Auto-imported"
    }
  }
  ,{
    id: 102,
    title: " Spvm3 Reelfind React Fastapi",
    year: 2026,
    category: "Web Applications & Portals",
    tagline: "-SPVM3-reelfind-react-fastapi",
    desc: "A full-stack movie and TV show discovery app built with React and FastAPI.",
    tech: ["Python", "FastAPI", "React"],
    live: "https://sanjaygl2006.vercel.app/",
    github: "https://github.com/sanjayGL2006/-SPVM3-reelfind-react-fastapi",
    status: "Completed",
    featured: false,
    icon: "fa-globe",
    stats: {
      "Type": "GitHub Project",
      "Source": "Auto-imported"
    }
  }
  ,{
    id: 103,
    title: "Spvm3 Spend Tracker",
    year: 2026,
    category: "Management & Enterprise Systems",
    tagline: "spvm3-spend-tracker",
    desc: "Fast, responsive finance and expense management dashboard built with React, Recharts, and FastAPI for SPVM³ Tech Solution.",
    tech: ["Python", "FastAPI", "React"],
    live: "https://sanjaygl2006.vercel.app/",
    github: "https://github.com/sanjayGL2006/spvm3-spend-tracker",
    status: "Completed",
    featured: false,
    icon: "fa-chart-line",
    stats: {
      "Type": "GitHub Project",
      "Source": "Auto-imported"
    }
  }
  ,{
    id: 104,
    title: "Fastapi React Todo",
    year: 2026,
    category: "Web Applications & Portals",
    tagline: "fastapi-react-todo",
    desc: "Full-stack interactive to-do app built with React (Vite) and FastAPI featuring priorities, inline editing, and status filtering.",
    tech: ["Python", "FastAPI", "React"],
    live: "https://sanjaygl2006.vercel.app/",
    github: "https://github.com/sanjayGL2006/fastapi-react-todo",
    status: "Completed",
    featured: false,
    icon: "fa-globe",
    stats: {
      "Type": "GitHub Project",
      "Source": "Auto-imported"
    }
  }
  ,{
    id: 105,
    title: "Spvm3 Task App",
    year: 2026,
    category: "Web Applications & Portals",
    tagline: "spvm3-task-app",
    desc: "SPVM³ Task App — A sleek, intuitive Kanban task manager featuring interactive drag-and-drop columns, priority indicators, and REST API integration with FastAPI & React.",
    tech: ["Python", "FastAPI", "React"],
    live: "https://sanjaygl2006.vercel.app/",
    github: "https://github.com/sanjayGL2006/spvm3-task-app",
    status: "Completed",
    featured: false,
    icon: "fa-globe",
    stats: {
      "Type": "GitHub Project",
      "Source": "Auto-imported"
    }
  }
  ,{
    id: 106,
    title: "Spvm3 Player",
    year: 2026,
    category: "Web Applications & Portals",
    tagline: "spvm3-player",
    desc: "Full-stack modern music player built with React 18, Vite, and FastAPI. Features automatic local library sync, ID3 metadata & album art extraction, sleek glassmorphic UI, audio visualizer, and HTTP …",
    tech: ["Python", "FastAPI", "React"],
    live: "https://sanjaygl2006.vercel.app/",
    github: "https://github.com/sanjayGL2006/spvm3-player",
    status: "Completed",
    featured: false,
    icon: "fa-globe",
    stats: {
      "Type": "GitHub Project",
      "Source": "Auto-imported"
    }
  }
  ,{
    id: 107,
    title: "Sentry Cyber Intel",
    year: 2026,
    category: "AI & Machine Learning",
    tagline: "sentry-cyber-intel",
    desc: "Multi-agent AI cybersecurity intelligence platform powered by CrewAI, Groq & Exa for automated threat intelligence research, CVE triage, and risk assessment.",
    tech: ["JavaScript", "HTML", "CSS"],
    live: "https://sanjaygl2006.vercel.app/",
    github: "https://github.com/sanjayGL2006/sentry-cyber-intel",
    status: "Completed",
    featured: false,
    icon: "fa-brain",
    stats: {
      "Type": "GitHub Project",
      "Source": "Auto-imported"
    }
  }
  ,{
    id: 108,
    title: "Milano Infotech Internship",
    year: 2026,
    category: "Web Applications & Portals",
    tagline: "Milano-infotech-internship",
    desc: "Python Updated 2 days ago",
    tech: ["Python", "FastAPI", "React"],
    live: "https://sanjaygl2006.vercel.app/",
    github: "https://github.com/sanjayGL2006/Milano-infotech-internship",
    status: "Completed",
    featured: false,
    icon: "fa-globe",
    stats: {
      "Type": "GitHub Project",
      "Source": "Auto-imported"
    }
  }
  ,{
    id: 109,
    title: "Spvm3 Code Notes",
    year: 2026,
    category: "Portfolios, Profiles & Tributes",
    tagline: "SPVM3-code-notes",
    desc: "Comprehensive Computer Science & Programming Notes Hub featuring interactive guides for 20+ technologies, code references, and an integrated certificate verification system.",
    tech: ["JavaScript", "HTML", "CSS"],
    live: "https://sanjaygl2006.vercel.app/",
    github: "https://github.com/sanjayGL2006/SPVM3-code-notes",
    status: "Completed",
    featured: false,
    icon: "fa-globe",
    stats: {
      "Type": "GitHub Project",
      "Source": "Auto-imported"
    }
  }
  ,{
    id: 110,
    title: "Spvm3 Code Editor",
    year: 2026,
    category: "Tools, Systems & Utilities",
    tagline: "spvm3-code-editor",
    desc: "Modular, local-first desktop IDE built on Electron, React & Monaco. Features multi-language runners (Python, Java, C/C++, C#), A-Z file support, Extensions Marketplace, multi-version Python selecto…",
    tech: ["Python", "FastAPI", "React"],
    live: "https://sanjaygl2006.vercel.app/",
    github: "https://github.com/sanjayGL2006/spvm3-code-editor",
    status: "Completed",
    featured: false,
    icon: "fa-tools",
    stats: {
      "Type": "GitHub Project",
      "Source": "Auto-imported"
    }
  }
  ,{
    id: 111,
    title: "Spvm3 Editor",
    year: 2026,
    category: "AI & Machine Learning",
    tagline: "spvm3-editor",
    desc: "Next-generation lightweight desktop IDE powered by Monaco Editor, integrated terminal runner, and offline-capable AI code intelligence.",
    tech: ["JavaScript", "HTML", "CSS"],
    live: "https://sanjaygl2006.vercel.app/",
    github: "https://github.com/sanjayGL2006/spvm3-editor",
    status: "Completed",
    featured: false,
    icon: "fa-brain",
    stats: {
      "Type": "GitHub Project",
      "Source": "Auto-imported"
    }
  }
  ,{
    id: 112,
    title: "Smart Attendance Yolo",
    year: 2026,
    category: "AI & Machine Learning",
    tagline: "smart-attendance-yolo",
    desc: "Real-time automated classroom attendance tracker powered by custom YOLOv8 computer vision, Flask REST API, MySQL, and an interactive React teacher dashboard.",
    tech: ["Python", "FastAPI", "React"],
    live: "https://sanjaygl2006.vercel.app/",
    github: "https://github.com/sanjayGL2006/smart-attendance-yolo",
    status: "Completed",
    featured: false,
    icon: "fa-brain",
    stats: {
      "Type": "GitHub Project",
      "Source": "Auto-imported"
    }
  }
  ,{
    id: 113,
    title: "Spvm3 Campus Placement",
    year: 2026,
    category: "AI & Machine Learning",
    tagline: "spvm3-campus-placement",
    desc: "An AI-powered campus placement & career intelligence suite: automated ATS resume analysis, skills gap roadmaps, safe AI natural language queries, and department-isolated analytics dashboards. Built…",
    tech: ["JavaScript", "HTML", "CSS"],
    live: "https://sanjaygl2006.vercel.app/",
    github: "https://github.com/sanjayGL2006/spvm3-campus-placement",
    status: "Completed",
    featured: false,
    icon: "fa-brain",
    stats: {
      "Type": "GitHub Project",
      "Source": "Auto-imported"
    }
  }
  ,{
    id: 114,
    title: "Placement Pro Spvm3",
    year: 2026,
    category: "Management & Enterprise Systems",
    tagline: "placement-pro-SPVM3",
    desc: "Smart College Placement & Campus Recruitment Management System built with Python Flask, PHP, Docker, Kubernetes & Vercel. Developed by SPVM3 Tech Solution by Sanjay G L.",
    tech: ["Python", "FastAPI", "React"],
    live: "https://sanjaygl2006.vercel.app/",
    github: "https://github.com/sanjayGL2006/placement-pro-SPVM3",
    status: "Completed",
    featured: false,
    icon: "fa-chart-line",
    stats: {
      "Type": "GitHub Project",
      "Source": "Auto-imported"
    }
  }
  ,{
    id: 115,
    title: "Spvm3 Car Game",
    year: 2026,
    category: "Games",
    tagline: "spvm3-car-game",
    desc: "Action-packed 2D physics racing game featuring 200-level stage progression, 60+ customizable vehicles, multi-layer parallax scenery, real-time audio synthesis, companion Python telemetry server, an…",
    tech: ["Python", "FastAPI", "React"],
    live: "https://sanjaygl2006.vercel.app/",
    github: "https://github.com/sanjayGL2006/spvm3-car-game",
    status: "Completed",
    featured: false,
    icon: "fa-gamepad",
    stats: {
      "Type": "GitHub Project",
      "Source": "Auto-imported"
    }
  }
  ,{
    id: 116,
    title: "Text2Img Studio",
    year: 2026,
    category: "AI & Machine Learning",
    tagline: "text2img-studio",
    desc: "A full-stack Flask web app for AI text-to-image generation powered by Stable Diffusion with built-in MySQL/SQLite generation history tracking.",
    tech: ["JavaScript", "HTML", "CSS"],
    live: "https://sanjaygl2006.vercel.app/",
    github: "https://github.com/sanjayGL2006/text2img-studio",
    status: "Completed",
    featured: false,
    icon: "fa-brain",
    stats: {
      "Type": "GitHub Project",
      "Source": "Auto-imported"
    }
  }
  ,{
    id: 117,
    title: "Small Project",
    year: 2026,
    category: "Web Applications & Portals",
    tagline: "small-project",
    desc: "A collection of small web projects, templates, and frontend experiments built with HTML, CSS, and JavaScript.",
    tech: ["JavaScript", "HTML", "CSS"],
    live: "https://sanjaygl2006.vercel.app/",
    github: "https://github.com/sanjayGL2006/small-project",
    status: "Completed",
    featured: false,
    icon: "fa-globe",
    stats: {
      "Type": "GitHub Project",
      "Source": "Auto-imported"
    }
  }
  ,{
    id: 118,
    title: "Spvm3 Tech Solution Websites",
    year: 2026,
    category: "Web Applications & Portals",
    tagline: "SPVM3-tech-solution-websites",
    desc: "HTML Updated last week",
    tech: ["JavaScript", "HTML", "CSS"],
    live: "https://sanjaygl2006.vercel.app/",
    github: "https://github.com/sanjayGL2006/SPVM3-tech-solution-websites",
    status: "Completed",
    featured: false,
    icon: "fa-globe",
    stats: {
      "Type": "GitHub Project",
      "Source": "Auto-imported"
    }
  }
  ,{
    id: 119,
    title: "Spvm3 Tech Solution",
    year: 2026,
    category: "Web Applications & Portals",
    tagline: "SPVM3-tech-solution",
    desc: "Python Updated last week",
    tech: ["Python", "FastAPI", "React"],
    live: "https://sanjaygl2006.vercel.app/",
    github: "https://github.com/sanjayGL2006/SPVM3-tech-solution",
    status: "Completed",
    featured: false,
    icon: "fa-globe",
    stats: {
      "Type": "GitHub Project",
      "Source": "Auto-imported"
    }
  }
  ,{
    id: 120,
    title: "Sanjay Gl Website Carbon Intelligence",
    year: 2026,
    category: "Tools, Systems & Utilities",
    tagline: "sanjay-gl-website-carbon-intelligence",
    desc: "SANJAY GL Website Carbon Intelligence — A real-time web application and developer API to audit website carbon footprints, HTTP page payload telemetry, energy consumption (SWD v4), and green hosting…",
    tech: ["JavaScript", "HTML", "CSS"],
    live: "https://sanjaygl2006.vercel.app/",
    github: "https://github.com/sanjayGL2006/sanjay-gl-website-carbon-intelligence",
    status: "Completed",
    featured: false,
    icon: "fa-tools",
    stats: {
      "Type": "GitHub Project",
      "Source": "Auto-imported"
    }
  }
  ,{
    id: 121,
    title: "Resume Analyzer",
    year: 2026,
    category: "AI & Machine Learning",
    tagline: "resume-analyzer",
    desc: "AI-powered resume match & skill gap analyzer built with Flask and MySQL. Uses TF-IDF vectorization to score resumes against job descriptions, highlight missing skills, and persist analysis results.",
    tech: ["JavaScript", "HTML", "CSS"],
    live: "https://sanjaygl2006.vercel.app/",
    github: "https://github.com/sanjayGL2006/resume-analyzer",
    status: "Completed",
    featured: false,
    icon: "fa-brain",
    stats: {
      "Type": "GitHub Project",
      "Source": "Auto-imported"
    }
  }
  ,{
    id: 122,
    title: "Image To Svg Converter",
    year: 2026,
    category: "Tools, Systems & Utilities",
    tagline: "image-to-svg-converter",
    desc: "A blazingly fast, client-side web & desktop tool to convert JPG, PNG, and WEBP images into clean, scalable SVG vector graphics with K-means color quantization, Bezier smoothing, and zero server upl…",
    tech: ["JavaScript", "HTML", "CSS"],
    live: "https://sanjaygl2006.vercel.app/",
    github: "https://github.com/sanjayGL2006/image-to-svg-converter",
    status: "Completed",
    featured: false,
    icon: "fa-tools",
    stats: {
      "Type": "GitHub Project",
      "Source": "Auto-imported"
    }
  }
  ,{
    id: 123,
    title: "Portfolio",
    year: 2026,
    category: "Portfolios, Profiles & Tributes",
    tagline: "portfolio",
    desc: "HTML Updated on Jul 7",
    tech: ["JavaScript", "HTML", "CSS"],
    live: "https://sanjaygl2006.vercel.app/",
    github: "https://github.com/sanjayGL2006/portfolio",
    status: "Completed",
    featured: false,
    icon: "fa-globe",
    stats: {
      "Type": "GitHub Project",
      "Source": "Auto-imported"
    }
  }
  ,{
    id: 124,
    title: " Handcrafted With Love Pure Weaves",
    year: 2026,
    category: "Web Applications & Portals",
    tagline: "-Handcrafted-with-Love-Pure-Weaves",
    desc: "HTML Updated on Jun 17",
    tech: ["JavaScript", "HTML", "CSS"],
    live: "https://pureweaves.vercel.app/",
    github: "https://github.com/sanjayGL2006/-Handcrafted-with-Love-Pure-Weaves",
    status: "Completed",
    featured: false,
    icon: "fa-globe",
    stats: {
      "Type": "GitHub Project",
      "Source": "Auto-imported"
    }
  }
  ,{
    id: 125,
    title: "Srimariyammatemple Ad2Fd3A5",
    year: 2026,
    category: "Portfolios, Profiles & Tributes",
    tagline: "srimariyammatemple-ad2fd3a5",
    desc: "TypeScript Updated on Apr 7",
    tech: ["JavaScript", "HTML", "CSS"],
    live: "https://sanjaygl2006.vercel.app/",
    github: "https://github.com/sanjayGL2006/srimariyammatemple-ad2fd3a5",
    status: "Completed",
    featured: false,
    icon: "fa-globe",
    stats: {
      "Type": "GitHub Project",
      "Source": "Auto-imported"
    }
  }
  ,{
    id: 126,
    title: "Temp Convert Web App",
    year: 2026,
    category: "Tools, Systems & Utilities",
    tagline: "temp-convert-web-app",
    desc: "A clean, mobile-responsive temperature converter built with HTML, CSS, and Vanilla JavaScript, featuring high-precision Celsius and Fahrenheit conversions.",
    tech: ["JavaScript", "HTML", "CSS"],
    live: "https://sanjaygl2006.vercel.app/",
    github: "https://github.com/sanjayGL2006/temp-convert-web-app",
    status: "Completed",
    featured: false,
    icon: "fa-tools",
    stats: {
      "Type": "GitHub Project",
      "Source": "Auto-imported"
    }
  }
  ,{
    id: 127,
    title: "Pure Weaves",
    year: 2026,
    category: "AI & Machine Learning",
    tagline: "Pure-Weaves",
    desc: "Gemini said Pure Weaves is a PHP/MySQL e-commerce platform for artisan sarees. It features a heritage-inspired UI, AJAX-powered cart, and a secure seller dashboard. Key highlights include real-time…",
    tech: ["JavaScript", "HTML", "CSS"],
    live: "https://pureweaves.vercel.app/",
    github: "https://github.com/sanjayGL2006/Pure-Weaves",
    status: "Completed",
    featured: false,
    icon: "fa-brain",
    stats: {
      "Type": "GitHub Project",
      "Source": "Auto-imported"
    }
  }
  ,{
    id: 128,
    title: "Sanjay G. L ",
    year: 2026,
    category: "Web Applications & Portals",
    tagline: "Sanjay-G.-L-",
    desc: "porfolio",
    tech: ["JavaScript", "HTML", "CSS"],
    live: "https://sanjaygl2006.vercel.app/",
    github: "https://github.com/sanjayGL2006/Sanjay-G.-L-",
    status: "Completed",
    featured: false,
    icon: "fa-globe",
    stats: {
      "Type": "GitHub Project",
      "Source": "Auto-imported"
    }
  },
  {
    id: "proj-auto-2d4c57c3",
    title: "Sanjay-G.-L-",
    year: 2026,
    category: "Web Applications & Portals",
    tagline: "Private portfolio, TypeScript",
    desc: "A software engineering project built by Sanjay G. L.",
    tech: ["Python", "JavaScript", "React", "HTML5"],
    live: "",
    github: "https://github.com/sanjayGL2006/Sanjay-G.-L-",
    status: "Completed",
    featured: false,
    icon: "fa-code",
    image: "assets/logo.svg",
    overview: "This project showcases my ability to develop full-stack solutions and software tools.",
    architecture: "Built with modern frameworks, focusing on modularity and clean code.",
    features: ["Responsive UI", "REST API Integration", "Clean Architecture"]
  }
];
