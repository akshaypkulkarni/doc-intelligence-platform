-- Initialize AI Document Platform Database
-- This script sets up the initial database structure

-- Create extensions if needed
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Create initial tables will be handled by Alembic migrations
-- This file is for any initial setup that needs to happen before migrations

-- Set timezone
SET timezone = 'UTC';
