-- Supabase PostgreSQL Schema for Portfolio Database

-- Create Projects Table
CREATE TABLE IF NOT EXISTS projects (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    year INTEGER,
    category VARCHAR(100),
    tagline TEXT,
    description TEXT,
    technologies TEXT, -- JSON string or comma separated
    live_url VARCHAR(500),
    github_url VARCHAR(500),
    status VARCHAR(50),
    featured BOOLEAN DEFAULT FALSE,
    icon VARCHAR(50),
    image VARCHAR(500),
    overview TEXT,
    architecture TEXT,
    features TEXT -- JSON string or comma separated
);

-- Create Certificates Table
CREATE TABLE IF NOT EXISTS certificates (
    id VARCHAR(100) PRIMARY KEY,
    type VARCHAR(50),
    category VARCHAR(100),
    title VARCHAR(255) NOT NULL,
    org VARCHAR(255),
    date VARCHAR(100),
    month VARCHAR(50),
    year INTEGER,
    duration VARCHAR(100),
    description TEXT,
    tags TEXT,
    skills_learned TEXT,
    credential_id VARCHAR(255),
    drive_id VARCHAR(255),
    verify_link VARCHAR(500),
    image VARCHAR(500),
    emoji VARCHAR(20),
    featured BOOLEAN DEFAULT FALSE
);

-- Create Agent Conversations Table
CREATE TABLE IF NOT EXISTS agent_conversations (
    id SERIAL PRIMARY KEY,
    session_id VARCHAR(100) NOT NULL,
    user_message TEXT NOT NULL,
    agent_response TEXT NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create Agent Project Suggestions Table
CREATE TABLE IF NOT EXISTS agent_project_suggestions (
    id SERIAL PRIMARY KEY,
    session_id VARCHAR(100) NOT NULL,
    suggested_project VARCHAR(255) NOT NULL,
    reasoning TEXT NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create Site Visits Table
CREATE TABLE IF NOT EXISTS site_visits (
    id SERIAL PRIMARY KEY,
    page VARCHAR(100) NOT NULL,
    referrer VARCHAR(255),
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create Contact Messages Table
CREATE TABLE IF NOT EXISTS contact_messages (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    subject VARCHAR(255) NOT NULL,
    message TEXT NOT NULL,
    encrypted_key TEXT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(50) DEFAULT 'unread'
);

-- Note: Ensure Row Level Security (RLS) is configured appropriately via the Supabase Dashboard
-- based on your application's access patterns.
