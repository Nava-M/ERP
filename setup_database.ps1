# Enterprise ERP System - Database Setup Script
# Run this script to create the PostgreSQL database

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Enterprise ERP System - Database Setup" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "This script will create the PostgreSQL database for the ERP system." -ForegroundColor Yellow
Write-Host ""

# Add PostgreSQL to PATH
$env:Path = $env:Path + ";C:\Program Files\PostgreSQL\18\bin"

# Prompt for postgres password
$postgresPassword = Read-Host "Enter PostgreSQL superuser (postgres) password" -AsSecureString
$BSTR = [System.Runtime.InteropServices.Marshal]::SecureStringToBSTR($postgresPassword)
$plainPassword = [System.Runtime.InteropServices.Marshal]::PtrToStringAuto($BSTR)

# Set password environment variable
$env:PGPASSWORD = $plainPassword

Write-Host ""
Write-Host "Creating database..." -ForegroundColor Green

# Run the SQL script
& psql -U postgres -f setup_database.sql

if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "========================================" -ForegroundColor Green
    Write-Host "Database setup complete!" -ForegroundColor Green
    Write-Host "========================================" -ForegroundColor Green
    Write-Host ""
    Write-Host "Database Name: erp_db" -ForegroundColor Cyan
    Write-Host "Database User: erp_user" -ForegroundColor Cyan
    Write-Host "Database Password: erp_password_123" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "IMPORTANT: The .env file has been updated with these credentials!" -ForegroundColor Yellow
    Write-Host ""
} else {
    Write-Host ""
    Write-Host "========================================" -ForegroundColor Red
    Write-Host "Database setup failed!" -ForegroundColor Red
    Write-Host "========================================" -ForegroundColor Red
    Write-Host ""
    Write-Host "Please check the error messages above." -ForegroundColor Yellow
    Write-Host ""
}

# Clear password from environment
$env:PGPASSWORD = $null

Write-Host "Press any key to continue..."
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
