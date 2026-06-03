"""
Reporting API URLs
"""
from django.urls import path
from .views import TrialBalanceView, BalanceSheetView, IncomeStatementView

urlpatterns = [
    path('trial-balance/', TrialBalanceView.as_view(), name='trial-balance'),
    path('balance-sheet/', BalanceSheetView.as_view(), name='balance-sheet'),
    path('income-statement/', IncomeStatementView.as_view(), name='income-statement'),
]
