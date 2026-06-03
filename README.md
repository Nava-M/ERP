# Enterprise ERP System - Finance Module

A comprehensive ERP system built with Django and PostgreSQL, combining SAP-level functionality with ERPNext-style simplicity.

## Project Status

**Phase 0: Backend Foundation** ✅ IN PROGRESS

- [x] Django project setup
- [x] Virtual environment created
- [x] All dependencies installed
- [x] Django apps created (12 apps)
- [x] Settings configured
- [x] Tenant models created
- [ ] PostgreSQL database setup
- [ ] Initial migrations
- [ ] Mock API endpoints
- [ ] API documentation

## Technology Stack

- **Backend**: Django 4.2.9, Python 3.12
- **Database**: PostgreSQL 16
- **API**: Django REST Framework
- **Multi-Tenancy**: django-tenants
- **Authentication**: JWT (djangorestframework-simplejwt)
- **Task Queue**: Celery + Redis
- **Frontend**: Vanilla HTML/CSS/JavaScript

## Project Structure

```
ERP/
├── .kiro/                      # Spec files (requirements, design, tasks)
├── venv/                       # Virtual environment
├── erp_system/                 # Django project settings
├── core/                       # Core utilities and base models
├── tenants/                    # Multi-tenancy management
├── accounts/                   # Chart of accounts
├── ledger/                     # General ledger, transactions
├── invoicing/                  # Customer invoices, vendor bills
├── payments/                   # Payment processing
├── tax/                        # Tax calculations
├── reporting/                  # Financial reports
├── budgeting/                  # Budget management
├── fixed_assets/               # Asset tracking
├── bank_reconciliation/        # Bank statement matching
├── expense_management/         # Expense tracking
├── manage.py                   # Django management script
├── requirements.txt            # Python dependencies
└── .env                        # Environment variables
```

## Setup Instructions

### 1. Prerequisites

- Python 3.12+
- PostgreSQL 16
- Redis (for Celery and caching)

### 2. Installation

```bash
# Clone the repository
cd C:\Users\HP\OneDrive\Desktop\ERP

# Create virtual environment (already done)
python -m venv venv

# Activate virtual environment
.\venv\Scripts\Activate.ps1  # Windows PowerShell
# or
.\venv\Scripts\activate.bat  # Windows CMD

# Install dependencies (already done)
pip install -r requirements.txt
```

### 3. Database Setup

```bash
# Create PostgreSQL database
psql -U postgres
CREATE DATABASE erp_db;
CREATE USER erp_user WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE erp_db TO erp_user;
\q

# Update .env file with your database credentials
```

### 4. Run Migrations

```bash
# Run migrations
python manage.py migrate_schemas --shared

# Create superuser
python manage.py createsuperuser
```

### 5. Run Development Server

```bash
# Start Django development server
python manage.py runserver

# Access at: http://localhost:8000
# Admin panel: http://localhost:8000/admin
# API docs: http://localhost:8000/api/docs/
```

## Development Workflow

### Phase 0: Backend Foundation (Week 1-2)
- ✅ Django project setup
- ⏳ PostgreSQL configuration
- ⏳ Mock API endpoints
- ⏳ API documentation

### Phase 1: Frontend Development (Week 3-10)
- Login & Dashboard
- Chart of Accounts UI
- Transaction Entry UI
- Financial Reports UI

### Phase 2: Backend Development (Week 11-18)
- Real business logic
- Double-entry bookkeeping
- Audit trail
- Security implementation

### Phase 3: Integration & Testing (Week 19-21)
- Frontend-backend integration
- End-to-end testing
- Performance optimization
- Production deployment

## Environment Variables

Create a `.env` file in the project root:

```env
# Django Settings
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database Settings
DB_NAME=erp_db
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432

# Redis Settings
REDIS_HOST=localhost
REDIS_PORT=6379

# JWT Settings
JWT_ACCESS_TOKEN_LIFETIME=15
JWT_REFRESH_TOKEN_LIFETIME=10080
```

## API Endpoints (Mock - Phase 0)

### Authentication
- `POST /api/v1/auth/login/` - User login
- `POST /api/v1/auth/logout/` - User logout
- `POST /api/v1/auth/refresh/` - Refresh JWT token

### Accounts
- `GET /api/v1/accounts/` - List accounts
- `POST /api/v1/accounts/` - Create account
- `GET /api/v1/accounts/{id}/` - Get account details
- `PUT /api/v1/accounts/{id}/` - Update account
- `DELETE /api/v1/accounts/{id}/` - Delete account

### Transactions
- `GET /api/v1/transactions/` - List transactions
- `POST /api/v1/transactions/` - Create transaction
- `GET /api/v1/transactions/{id}/` - Get transaction details

### Reports
- `GET /api/v1/reports/trial-balance/` - Trial balance report
- `GET /api/v1/reports/balance-sheet/` - Balance sheet report
- `GET /api/v1/reports/income-statement/` - Income statement report

## Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=.

# Run specific test file
pytest accounts/tests/test_models.py
```

## Code Quality

```bash
# Format code with black
black .

# Sort imports
isort .

# Lint code
pylint */

# Type checking
mypy .
```

## Contributing

1. Create a feature branch
2. Make your changes
3. Run tests and linting
4. Submit a pull request

## License

Proprietary - All rights reserved

## Contact

For questions or support, contact the development team.
