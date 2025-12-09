#!/bin/sh
# wait-for-postgres.sh

set -e

# Use DB_HOST and DB_PORT from the environment variables set in the ECS task definition
HOST=$DB_HOST
PORT=${DB_PORT:-5432} # Default to 5432 if DB_PORT is not set

# The `pg_isready` command is part of the `postgresql-client` package installed in the Dockerfile.
# It checks if a PostgreSQL server is accepting connections.
# We loop until the database is ready, sleeping for a few seconds between attempts.
while ! pg_isready -h "$HOST" -p "$PORT" -q; do
    echo "$(date) - waiting for database to start at $HOST:$PORT"
    sleep 2
done

echo "Database is ready!"
