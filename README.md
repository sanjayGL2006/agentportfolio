# Sanjay G. L. — Developer Portfolio & Flask Backend

A modern, high-performance developer portfolio built with HTML5, CSS3, JavaScript, and Python Flask. Features 23 showcase projects, 102 verified certificates, 3D card flips, glassmorphism UI, theme toggle, command palette (`Ctrl+K`), and an interactive Floating AI Robot Assistant.

## Features
- **Floating AI Assistant (Robot/Fox Widget)**: Answers questions about Sanjay's skills, projects, background, and contact details with local storage history.
- **3D Flip Card Projects Showcase**: 23 interactive project cards with live demo and GitHub repository links.
- **102 Verified Certificates Gallery**: Filterable archive with Google Drive preview modal and HackerRank filter.
- **Python Flask API & Backend**:
  - `GET /api/about`: Profile JSON payload.
  - `POST /chat`: Intelligent Q&A bot endpoint.
  - `POST /api/contact`: Form submission handling.
- **Command Palette (`Ctrl+K`)**: Quick fuzzy navigation and shortcuts.
- **Dark/Light Theme Toggle**: System preference memory.

## How to Run Locally

1. Install Python 3.9+
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Start the Flask application:
   ```bash
   python app.py
   ```
4. Open your browser at `http://localhost:5000`

