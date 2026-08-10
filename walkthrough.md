# Walkthrough: Docker and Vercel Setup Completed

The Docker configuration and Vercel deployment files have been successfully created and verified for syntax.

## Changes Made

1. **[Dockerfile](file:///c:/Users/Sanjay%20G%20L/Desktop/portfolio/Dockerfile)**: Standard multi-stage structure utilizing `python:3.11-slim` and Gunicorn to run the Flask application.
2. **[.dockerignore](file:///c:/Users/Sanjay%20G%20L/Desktop/portfolio/.dockerignore)**: Ignores node modules, virtual environments, cache, and metadata files.
3. **[vercel.json](file:///c:/Users/Sanjay%20G%20L/Desktop/portfolio/vercel.json)**: Configures Vercel to route all dynamic traffic to the entrypoint file and use Vercel's Python runtime.
4. **[api/index.py](file:///c:/Users/Sanjay%20G%20L/Desktop/portfolio/api/index.py)**: Imports the Flask `app` instance from `app.py` in the parent directory and acts as Vercel's serverless entry point.
5. **[requirements.txt](file:///c:/Users/Sanjay%20G%20L/Desktop/portfolio/requirements.txt)**: Added `pypdf` dependency for parsing PDF certificates.

---

## Deployment and Verification Instructions

### 1. Running via Docker

To build the image and run the application in a local container (requires Docker Desktop to be running):

```powershell
# 1. Build the Docker image
docker build -t portfolio-app .

# 2. Run the container on port 5000
docker run -d -p 5000:5000 --name portfolio-container portfolio-app
```

Once running, open `http://localhost:5000` to access the application.

### 2. Hosting on Vercel

To host this repository on Vercel:

1. **Push your code** to a GitHub repository.
2. **Import your project** in the [Vercel Dashboard](https://vercel.com/new).
3. Vercel will automatically detect `vercel.json` and deploy your Flask app and static assets.

Alternatively, you can deploy using the Vercel CLI from your terminal:
```powershell
# Install Vercel CLI globally
npm install -g vercel

# Deploy (login and setup)
vercel --prod
```

---

## AI Chatbot Database Integration & MySQL Support

### 1. Database Persistence
- Every question asked by visitors via the chat panel is logged in the `agent_conversations` database table using dynamic ORM queries in `app.py`.
- If an internship project suggestion is triggered, those ideas and reasoning are logged into `agent_project_suggestions`.

### 2. Administrative Tools
- **[view_agent_conversations.py](file:///c:/Users/Sanjay%20G%20L/Desktop/portfolio/view_agent_conversations.py)**: A new CLI tool to display all question-and-answer interactions stored in the database.
- **[.env.example](file:///c:/Users/Sanjay%20G%20L/Desktop/portfolio/.env.example)**: A configuration guide showing how to set up environment parameters to switch from the default local SQLite database to a production MySQL database instance.

