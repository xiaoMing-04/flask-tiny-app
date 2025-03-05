#!/bin/bash

# Apply migrations
echo "Applying database migrations..."
python manage.py migrate

# Collect static files (nếu cần)
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Chạy server
echo "Starting Django server..."
exec python manage.py runserver 0.0.0.0:8000