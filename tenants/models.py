from django.db import models
from django_tenants.models import TenantMixin, DomainMixin


class Tenant(TenantMixin):
    """
    Tenant model for multi-tenancy support.
    Each tenant represents a separate organization/company.
    """
    name = models.CharField(max_length=255)
    base_currency = models.CharField(max_length=3, default='USD')
    fiscal_year_start = models.DateField()
    timezone = models.CharField(max_length=50, default='UTC')
    locale = models.CharField(max_length=10, default='en-US')
    status = models.CharField(
        max_length=20,
        choices=[
            ('active', 'Active'),
            ('suspended', 'Suspended'),
            ('deleted', 'Deleted')
        ],
        default='active'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # django-tenants will automatically create schema
    auto_create_schema = True

    class Meta:
        db_table = 'tenants'

    def __str__(self):
        return self.name


class Domain(DomainMixin):
    """
    Domain model for tenant routing.
    Maps domains/subdomains to tenants.
    """
    pass
