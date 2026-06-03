"""
Accounts API URLs
"""
from django.urls import path
from .views import AccountListView, AccountDetailView

urlpatterns = [
    path('', AccountListView.as_view(), name='account-list'),
    path('<uuid:pk>/', AccountDetailView.as_view(), name='account-detail'),
]
