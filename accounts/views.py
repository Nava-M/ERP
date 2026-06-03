"""
Accounts API Views (Mock Data for Phase 0)
"""
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema, OpenApiResponse
import uuid


# Mock data for Phase 0
MOCK_ACCOUNTS = [
    {
        'id': str(uuid.uuid4()),
        'account_number': '1000',
        'name': 'Cash',
        'account_type': 'asset',
        'account_subtype': 'current_asset',
        'currency': 'USD',
        'balance': 50000.00,
        'is_active': True,
    },
    {
        'id': str(uuid.uuid4()),
        'account_number': '1100',
        'name': 'Accounts Receivable',
        'account_type': 'asset',
        'account_subtype': 'current_asset',
        'currency': 'USD',
        'balance': 25000.00,
        'is_active': True,
    },
    {
        'id': str(uuid.uuid4()),
        'account_number': '2000',
        'name': 'Accounts Payable',
        'account_type': 'liability',
        'account_subtype': 'current_liability',
        'currency': 'USD',
        'balance': 15000.00,
        'is_active': True,
    },
    {
        'id': str(uuid.uuid4()),
        'account_number': '4000',
        'name': 'Sales Revenue',
        'account_type': 'revenue',
        'account_subtype': 'operating_revenue',
        'currency': 'USD',
        'balance': 100000.00,
        'is_active': True,
    },
    {
        'id': str(uuid.uuid4()),
        'account_number': '5000',
        'name': 'Cost of Goods Sold',
        'account_type': 'expense',
        'account_subtype': 'cost_of_goods_sold',
        'currency': 'USD',
        'balance': 40000.00,
        'is_active': True,
    },
]


class AccountListView(APIView):
    """
    List all accounts or create a new account (Mock)
    """
    permission_classes = [IsAuthenticated]
    
    @extend_schema(
        responses={200: OpenApiResponse(description='List of accounts')}
    )
    def get(self, request):
        """
        Get list of all accounts
        """
        return Response({
            'count': len(MOCK_ACCOUNTS),
            'results': MOCK_ACCOUNTS
        })
    
    @extend_schema(
        request={
            'application/json': {
                'type': 'object',
                'properties': {
                    'account_number': {'type': 'string'},
                    'name': {'type': 'string'},
                    'account_type': {'type': 'string'},
                    'currency': {'type': 'string'},
                },
                'required': ['account_number', 'name', 'account_type']
            }
        },
        responses={
            201: OpenApiResponse(description='Account created'),
            400: OpenApiResponse(description='Invalid data'),
        }
    )
    def post(self, request):
        """
        Create a new account (Mock - returns success)
        """
        data = request.data
        new_account = {
            'id': str(uuid.uuid4()),
            'account_number': data.get('account_number'),
            'name': data.get('name'),
            'account_type': data.get('account_type'),
            'account_subtype': data.get('account_subtype', 'current_asset'),
            'currency': data.get('currency', 'USD'),
            'balance': 0.00,
            'is_active': True,
        }
        return Response(new_account, status=status.HTTP_201_CREATED)


class AccountDetailView(APIView):
    """
    Retrieve, update or delete an account (Mock)
    """
    permission_classes = [IsAuthenticated]
    
    @extend_schema(
        responses={
            200: OpenApiResponse(description='Account details'),
            404: OpenApiResponse(description='Account not found'),
        }
    )
    def get(self, request, pk):
        """
        Get account details
        """
        # Return first account as mock
        if MOCK_ACCOUNTS:
            account = MOCK_ACCOUNTS[0].copy()
            account['id'] = str(pk)
            return Response(account)
        return Response(
            {'error': 'Account not found'},
            status=status.HTTP_404_NOT_FOUND
        )
    
    @extend_schema(
        request={
            'application/json': {
                'type': 'object',
                'properties': {
                    'name': {'type': 'string'},
                    'is_active': {'type': 'boolean'},
                }
            }
        },
        responses={
            200: OpenApiResponse(description='Account updated'),
            404: OpenApiResponse(description='Account not found'),
        }
    )
    def put(self, request, pk):
        """
        Update account (Mock - returns success)
        """
        if MOCK_ACCOUNTS:
            account = MOCK_ACCOUNTS[0].copy()
            account['id'] = str(pk)
            account.update(request.data)
            return Response(account)
        return Response(
            {'error': 'Account not found'},
            status=status.HTTP_404_NOT_FOUND
        )
    
    @extend_schema(
        responses={
            204: OpenApiResponse(description='Account deleted'),
            404: OpenApiResponse(description='Account not found'),
        }
    )
    def delete(self, request, pk):
        """
        Delete account (Mock - returns success)
        """
        return Response(status=status.HTTP_204_NO_CONTENT)
