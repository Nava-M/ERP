#!/usr/bin/env python
"""
Script to create a Django superuser programmatically
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'erp_system.settings')
django.setup()

from django.contrib.auth.models import User

# Create superuser if it doesn't exist
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser(
        username='admin',
        email='admin@example.com',
        password='admin123'
    )
    print("✅ Superuser created successfully!")
    print("   Username: admin")
    print("   Password: admin123")
    print("   Email: admin@example.com")
else:
    print("⚠️  Superuser 'admin' already exists!")
