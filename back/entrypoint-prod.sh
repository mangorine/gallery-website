#!/bin/sh

echo "Starting celery..."
celery -A galerie worker --loglevel=info --logfile=/var/log/celery.log --detach

echo "Checking deployment..."
python3 manage.py check --deploy

echo "Copying static files..."
python3 manage.py collectstatic --noinput

echo "Check if PostgreSQL started..."
while ! nc -z $DB_HOST $DB_PORT; do
    sleep 0.1
done
echo "PostgreSQL started."

echo "Migrating..."
python3 manage.py migrate --noinput

echo "Starting gunicorn server..."

exec "$@"