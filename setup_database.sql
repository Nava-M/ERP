-- Database setup script for Enterprise ERP System
-- Run this script as the postgres superuser

-- Create database
CREATE DATABASE erp_db;

-- Create user (change password as needed)
CREATE USER erp_user WITH PASSWORD 'erp_password_123';

-- Grant privileges
GRANT ALL PRIVILEGES ON DATABASE erp_db TO erp_user;

-- Connect to the database
\c erp_db

-- Grant schema privileges
GRANT ALL ON SCHEMA public TO erp_user;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO erp_user;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO erp_user;

-- Set default privileges for future tables
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON TABLES TO erp_user;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON SEQUENCES TO erp_user;

-- Verify
SELECT current_database();
