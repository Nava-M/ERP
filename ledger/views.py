"""
Ledger (Transactions) API Views (Mock Data for Phase 0)
"""
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema, OpenApiResponse
import uuid
from datetime import date


# Mock data for Phase 0
MOCK_TRANSACTIONS = [
    {
        'id': str(uuid.uuid4()),
        'transaction_number': 'TXN-00000001',
        'transaction_date': '2024-01-15',
        'description': 'Sale of goods',
        'status': 'posted',
        'currency': 'USD',
        'total_amount': 1000.00,
        'entries': [
            {
                'account': 'Cash',
                'debit_amount': 1000.00,
                'credit_amount': 0.00,
            },
            {
                'account': 'Sales Revenue',
                'debit_amount': 0.00,
                'credit_amount': 1000.00,
            }
        ]
    },
    {
        'id': str(uuid.uuid4()),
        'transaction_number': 'TXN-00000002',
        'transaction_date': '2024-01-16',
        'description': 'Purchase of inventory',
        'status': 'posted',
        'currency': 'USD',
        'total_amount': 500.00,
        'entries': [
            {
                'account': 'Inventory',
                'debit_amount': 500.00,
                'credit_amount': 0.00,
            },
            {
                'account': 'Cash',
                'debit_amount': 0.00,
                'credit_amount': 500.00,
            }
        ]
    },
]


class TransactionListView(APIView):
    """
    List all transactions or create a new transaction (Mock)
    """
    permission_classes = [IsAuthenticated]
    
    @extend_schema(
        responses={200: OpenApiResponse(description='List of transactions')}
    )
    def get(self, request):
        """
        Get list of all transactions
        """
        return Response({
            'count': len(MOCK_TRANSACTIONS),
            'results': MOCK_TRANSACTIONS
        })
    
    @extend_schema(
        request={
            'application/json': {
                'type': 'object',
                'properties': {
                    'transaction_date': {'type': 'string', 'format': 'date'},
                    'description': {'type': 'string'},
                    'entries': {
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'account_id': {'type': 'string'},
                                'debit_amount': {'type': 'number'},
                                'credit_amount': {'type': 'number'},
                            }
                        }
                    }
                },
                'required': ['transaction_date', 'description', 'entries']
            }
        },
        responses={
            201: OpenApiResponse(description='Transaction created'),
            400: OpenApiResponse(description='Invalid data'),
        }
    )
    def post(self, request):
        """
        Create a new transaction (Mock - returns success)
        """
        data = request.data
        new_transaction = {
            'id': str(uuid.uuid4()),
            'transaction_number': f'TXN-{str(uuid.uuid4())[:8]}',
            'transaction_date': data.get('transaction_date', str(date.today())),
            'description': data.get('description'),
            'status': 'draft',
            'currency': 'USD',
            'entries': data.get('entries', [])
        }
        return Response(new_transaction, status=status.HTTP_201_CREATED)


class TransactionDetailView(APIView):
    """
    Retrieve, update or delete a transaction (Mock)
    """
    permission_classes = [IsAuthenticated]
    
    @extend_schema(
        responses={
            200: OpenApiResponse(description='Transaction details'),
            404: OpenApiResponse(description='Transaction not found'),
        }
    )
    def get(self, request, pk):
        """
        Get transaction details
        """
        if MOCK_TRANSACTIONS:
            transaction = MOCK_TRANSACTIONS[0].copy()
            transaction['id'] = str(pk)
            return Response(transaction)
        return Response(
            {'error': 'Transaction not found'},
            status=status.HTTP_404_NOT_FOUND
        )
