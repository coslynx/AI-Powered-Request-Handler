#!/bin/bash

# Function to set up database connection
setup_database() {
  docker-compose up -d db
  until docker-compose exec db pg_isready; do
    echo "Waiting for PostgreSQL to start..."
    sleep 2
  done
  docker-compose exec app alembic upgrade head
}

# Function to start the application
start_application() {
  uvicorn api.src.main:app --reload
}

# Function to start Celery worker for background tasks
start_celery() {
  celery -A api.celery worker -l info
}

# Ensure environment variables are set
if [ -f .env ]; then
  source .env
fi

# Set up database connection if it's not already available
if ! docker-compose ps -q db; then
  setup_database
fi

# Start the application
start_application

# Optionally, start the Celery worker
start_celery