"""
Core API URLs - Routes to all module APIs
"""
from django.urls import path, include

urlpatterns = [
    # Authentication endpoints
    path('auth/', include('core.api.auth_urls')),
    
    # Finance module endpoints
    path('accounts/', include('accounts.urls')),
    path('transactions/', include('ledger.urls')),
    path('reports/', include('reporting.urls')),
]
