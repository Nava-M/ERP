# API Endpoints Documentation

## Base URL
- Development: `http://localhost:8000/api/v1/`
- API Documentation: `http://localhost:8000/api/docs/`

## Authentication Endpoints

### Login
- **POST** `/api/v1/auth/login/`
- **Description**: Authenticate user and receive JWT tokens
- **Request Body**:
```json
{
  "username": "string",
  "password": "string"
}
```
- **Response** (200 OK):
```json
{
  "refresh": "string (JWT refresh token)",
  "access": "string (JWT access token)",
  "user": {
    "id": "integer",
    "username": "string",
    "email": "string"
  }
}
```

### Logout
- **POST** `/api/v1/auth/logout/`
- **Description**: Blacklist refresh token
- **Headers**: `Authorization: Bearer <access_token>`
- **Request Body**:
```json
{
  "refresh": "string (JWT refresh token)"
}
```
- **Response** (205 Reset Content): No content

### Token Refresh
- **POST** `/api/v1/auth/refresh/`
- **Description**: Get new access token using refresh token
- **Request Body**:
```json
{
  "refresh": "string (JWT refresh token)"
}
```
- **Response** (200 OK):
```json
{
  "access": "string (new JWT access token)"
}
```

## Accounts Endpoints

### List Accounts
- **GET** `/api/v1/accounts/`
- **Description**: Get list of all accounts
- **Headers**: `Authorization: Bearer <access_token>`
- **Query Parameters**:
  - `page`: Page number (default: 1)
  - `page_size`: Items per page (default: 50)
  - `search`: Search by account name or number
  - `account_type`: Filter by account type
- **Response** (200 OK):
```json
{
  "count": 5,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "account_number": "1000",
      "name": "Cash",
      "type": "asset",
      "subtype": "current_asset",
      "balance": 50000.00,
      "currency": "USD",
      "parent": null,
      "is_active": true
    }
  ]
}
```

### Create Account
- **POST** `/api/v1/accounts/`
- **Description**: Create a new account
- **Headers**: `Authorization: Bearer <access_token>`
- **Request Body**:
```json
{
  "account_number": "string",
  "name": "string",
  "type": "asset|liability|equity|revenue|expense",
  "subtype": "string",
  "currency": "string (3-letter code)",
  "parent": "integer (optional)",
  "description": "string (optional)"
}
```
- **Response** (201 Created): Account object

### Get Account Details
- **GET** `/api/v1/accounts/{id}/`
- **Description**: Get details of a specific account
- **Headers**: `Authorization: Bearer <access_token>`
- **Response** (200 OK): Account object

### Update Account
- **PUT** `/api/v1/accounts/{id}/`
- **Description**: Update an existing account
- **Headers**: `Authorization: Bearer <access_token>`
- **Request Body**: Same as Create Account
- **Response** (200 OK): Updated account object

### Delete Account
- **DELETE** `/api/v1/accounts/{id}/`
- **Description**: Delete an account (soft delete)
- **Headers**: `Authorization: Bearer <access_token>`
- **Response** (204 No Content)

## Transaction Endpoints

### List Transactions
- **GET** `/api/v1/transactions/`
- **Description**: Get list of all transactions
- **Headers**: `Authorization: Bearer <access_token>`
- **Query Parameters**:
  - `page`: Page number
  - `page_size`: Items per page
  - `date_from`: Filter by start date (YYYY-MM-DD)
  - `date_to`: Filter by end date (YYYY-MM-DD)
  - `status`: Filter by status (draft|posted|void)
- **Response** (200 OK):
```json
{
  "count": 2,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "transaction_number": "JE-2024-001",
      "date": "2024-01-15",
      "description": "Initial capital investment",
      "status": "posted",
      "total_debit": 100000.00,
      "total_credit": 100000.00,
      "entries": [
        {
          "account": 1,
          "account_name": "Cash",
          "debit": 100000.00,
          "credit": 0.00,
          "description": "Cash received"
        },
        {
          "account": 3,
          "account_name": "Owner's Equity",
          "debit": 0.00,
          "credit": 100000.00,
          "description": "Capital contribution"
        }
      ]
    }
  ]
}
```

### Create Transaction
- **POST** `/api/v1/transactions/`
- **Description**: Create a new journal entry
- **Headers**: `Authorization: Bearer <access_token>`
- **Request Body**:
```json
{
  "date": "YYYY-MM-DD",
  "description": "string",
  "reference": "string (optional)",
  "entries": [
    {
      "account": "integer (account ID)",
      "debit": "decimal",
      "credit": "decimal",
      "description": "string (optional)"
    }
  ]
}
```
- **Validation**: Total debits must equal total credits
- **Response** (201 Created): Transaction object

### Get Transaction Details
- **GET** `/api/v1/transactions/{id}/`
- **Description**: Get details of a specific transaction
- **Headers**: `Authorization: Bearer <access_token>`
- **Response** (200 OK): Transaction object with entries

### Post Transaction
- **POST** `/api/v1/transactions/{id}/post/`
- **Description**: Post a draft transaction (make it permanent)
- **Headers**: `Authorization: Bearer <access_token>`
- **Response** (200 OK): Updated transaction object

### Void Transaction
- **POST** `/api/v1/transactions/{id}/void/`
- **Description**: Void a posted transaction
- **Headers**: `Authorization: Bearer <access_token>`
- **Response** (200 OK): Voided transaction object

## Report Endpoints

### Trial Balance
- **GET** `/api/v1/reports/trial-balance/`
- **Description**: Generate trial balance report
- **Headers**: `Authorization: Bearer <access_token>`
- **Query Parameters**:
  - `as_of_date`: Report date (YYYY-MM-DD, default: today)
- **Response** (200 OK):
```json
{
  "report_date": "2024-01-31",
  "accounts": [
    {
      "account_number": "1000",
      "account_name": "Cash",
      "debit": 50000.00,
      "credit": 0.00,
      "balance": 50000.00
    }
  ],
  "total_debits": 150000.00,
  "total_credits": 150000.00
}
```

### Balance Sheet
- **GET** `/api/v1/reports/balance-sheet/`
- **Description**: Generate balance sheet report
- **Headers**: `Authorization: Bearer <access_token>`
- **Query Parameters**:
  - `as_of_date`: Report date (YYYY-MM-DD, default: today)
- **Response** (200 OK):
```json
{
  "report_date": "2024-01-31",
  "assets": {
    "current_assets": [
      {
        "account": "Cash",
        "amount": 50000.00
      }
    ],
    "total_current_assets": 50000.00,
    "total_assets": 50000.00
  },
  "liabilities": {
    "current_liabilities": [],
    "total_liabilities": 0.00
  },
  "equity": {
    "items": [
      {
        "account": "Owner's Equity",
        "amount": 50000.00
      }
    ],
    "total_equity": 50000.00
  },
  "total_liabilities_and_equity": 50000.00
}
```

### Income Statement
- **GET** `/api/v1/reports/income-statement/`
- **Description**: Generate income statement (P&L) report
- **Headers**: `Authorization: Bearer <access_token>`
- **Query Parameters**:
  - `date_from`: Start date (YYYY-MM-DD)
  - `date_to`: End date (YYYY-MM-DD)
- **Response** (200 OK):
```json
{
  "period_start": "2024-01-01",
  "period_end": "2024-01-31",
  "revenue": {
    "items": [
      {
        "account": "Sales Revenue",
        "amount": 25000.00
      }
    ],
    "total_revenue": 25000.00
  },
  "expenses": {
    "items": [
      {
        "account": "Rent Expense",
        "amount": 5000.00
      }
    ],
    "total_expenses": 5000.00
  },
  "net_income": 20000.00
}
```

## Error Responses

### 400 Bad Request
```json
{
  "error": "Validation error message",
  "details": {
    "field_name": ["Error message"]
  }
}
```

### 401 Unauthorized
```json
{
  "detail": "Authentication credentials were not provided."
}
```

### 403 Forbidden
```json
{
  "detail": "You do not have permission to perform this action."
}
```

### 404 Not Found
```json
{
  "detail": "Not found."
}
```

### 500 Internal Server Error
```json
{
  "error": "Internal server error",
  "message": "An unexpected error occurred"
}
```

## Authentication

All endpoints except `/api/v1/auth/login/` and `/api/v1/auth/refresh/` require authentication.

Include the JWT access token in the Authorization header:
```
Authorization: Bearer <access_token>
```

Access tokens expire after 15 minutes. Use the refresh token to get a new access token.

## Rate Limiting

API endpoints are rate-limited to prevent abuse:
- Authentication endpoints: 5 requests per minute
- Other endpoints: 100 requests per minute

## Pagination

List endpoints support pagination:
- Default page size: 50 items
- Maximum page size: 100 items
- Use `page` and `page_size` query parameters

## Interactive Documentation

Visit `http://localhost:8000/api/docs/` for interactive Swagger UI documentation where you can test all endpoints.
