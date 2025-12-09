#!/bin/sh

# Exit immediately if a command exits with a non-zero status.
set -e

# Wait for the database to be ready before proceeding.
# The script now uses environment variables (DB_HOST, DB_PORT) set in the ECS task definition.
echo "Waiting for database..."
sh ./wait-for-postgres.sh

# Apply database migrations. This is a good practice to ensure the database
# schema is up to date with the application's models.
echo "Applying database migrations..."
python manage.py migrate

# Start the Gunicorn server.
# Gunicorn is a production-grade WSGI server.
# -w 4: Spawns 4 worker processes. Adjust this based on your CPU/memory resources.
# -b 0.0.0.0:8001: Binds the server to port 8001 on all network interfaces,
# making it accessible from outside the container. This matches the port in the ECS task definition.
# pretest.wsgi: Points Gunicorn to the WSGI application object in your project.
echo "Starting Gunicorn server..."
gunicorn pretest.wsgi:application -w 4 -b 0.0.0.0:8001
