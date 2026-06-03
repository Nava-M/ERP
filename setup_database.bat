@echo off
echo ========================================
echo Enterprise ERP System - Database Setup
echo ========================================
echo.
echo This script will create the PostgreSQL database for the ERP system.
echo.
echo Please enter your PostgreSQL superuser (postgres) password when prompted.
echo.
pause

"C:\Program Files\PostgreSQL\18\bin\psql.exe" -U postgres -f setup_database.sql

echo.
echo ========================================
echo Database setup complete!
echo ========================================
echo.
echo Database Name: erp_db
echo Database User: erp_user
echo Database Password: erp_password_123
echo.
echo IMPORTANT: Update your .env file with these credentials!
echo.
pause
