#!/bin/sh

echo "------ create default admin user ------"
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@myapp.local', 'Passw0rd')" | python manage.py shell