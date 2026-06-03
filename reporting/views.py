"""
Reporting API Views (Mock Data for Phase 0)
"""
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema, OpenApiResponse


class TrialBalanceView(APIView):
    """
    Trial Balance Report (Mock)
    """
    permission_classes = [IsAuthenticated]
    
    @extend_schema(
        responses={200: OpenApiResponse(description='Trial balance report')}
    )
    def get(self, request):
        """
        Get trial balance report
        """
        mock_data = {
            'report_date': '2024-01-31',
            'accounts': [
                {
                    'account_number': '1000',
                    'account_name': 'Cash',
                    'debit': 50000.00,
                    'credit': 0.00,
                },
                {
                    'account_number': '1100',
                    'account_name': 'Accounts Receivable',
                    'debit': 25000.00,
                    'credit': 0.00,
                },
                {
                    'account_number': '2000',
                    'account_name': 'Accounts Payable',
                    'debit': 0.00,
                    'credit': 15000.00,
                },
                {
                    'account_number': '4000',
                    'account_name': 'Sales Revenue',
                    'debit': 0.00,
                    'credit': 100000.00,
                },
                {
                    'account_number': '5000',
                    'account_name': 'Cost of Goods Sold',
                    'debit': 40000.00,
                    'credit': 0.00,
                },
            ],
            'total_debits': 115000.00,
            'total_credits': 115000.00,
        }
        return Response(mock_data)


class BalanceSheetView(APIView):
    """
    Balance Sheet Report (Mock)
    """
    permission_classes = [IsAuthenticated]
    
    @extend_schema(
        responses={200: OpenApiResponse(description='Balance sheet report')}
    )
    def get(self, request):
        """
        Get balance sheet report
        """
        mock_data = {
            'report_date': '2024-01-31',
            'assets': {
                'current_assets': [
                    {'name': 'Cash', 'amount': 50000.00},
                    {'name': 'Accounts Receivable', 'amount': 25000.00},
                ],
                'total_current_assets': 75000.00,
                'fixed_assets': [],
                'total_fixed_assets': 0.00,
                'total_assets': 75000.00,
            },
            'liabilities': {
                'current_liabilities': [
                    {'name': 'Accounts Payable', 'amount': 15000.00},
                ],
                'total_current_liabilities': 15000.00,
                'long_term_liabilities': [],
                'total_long_term_liabilities': 0.00,
                'total_liabilities': 15000.00,
            },
            'equity': {
                'items': [
                    {'name': 'Retained Earnings', 'amount': 60000.00},
                ],
                'total_equity': 60000.00,
            },
            'total_liabilities_and_equity': 75000.00,
        }
        return Response(mock_data)


class IncomeStatementView(APIView):
    """
    Income Statement Report (Mock)
    """
    permission_classes = [IsAuthenticated]
    
    @extend_schema(
        responses={200: OpenApiResponse(description='Income statement report')}
    )
    def get(self, request):
        """
        Get income statement report
        """
        mock_data = {
            'period_start': '2024-01-01',
            'period_end': '2024-01-31',
            'revenue': {
                'items': [
                    {'name': 'Sales Revenue', 'amount': 100000.00},
                ],
                'total_revenue': 100000.00,
            },
            'expenses': {
                'items': [
                    {'name': 'Cost of Goods Sold', 'amount': 40000.00},
                    {'name': 'Operating Expenses', 'amount': 20000.00},
                ],
                'total_expenses': 60000.00,
            },
            'net_income': 40000.00,
        }
        return Response(mock_data)
