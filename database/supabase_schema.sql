-- Enable the pgvector and uuid extensions for deep learning embeddings & unique log IDs
CREATE EXTENSION IF NOT EXISTS vector;
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Create the table to store AIOS interactions & continuous learning logs
CREATE TABLE IF NOT EXISTS aios_chat_logs (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    session_id VARCHAR(255),
    user_query TEXT NOT NULL,
    agent_response TEXT NOT NULL,
    query_embedding vector(1536), -- Neural network vector representation for RAG / auto-training
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Enable Row Level Security (RLS) to protect data
ALTER TABLE aios_chat_logs ENABLE ROW LEVEL SECURITY;

-- Policies for insertion and querying
CREATE POLICY "Allow public insert" ON aios_chat_logs FOR INSERT WITH CHECK (true);
CREATE POLICY "Allow public select" ON aios_chat_logs FOR SELECT USING (true);
