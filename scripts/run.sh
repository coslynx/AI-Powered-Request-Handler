#!/bin/bash

# Function to load environment variables
load_environment_variables() {
  if [ -f .env ]; then
    source .env
    echo "[INFO] Environment variables loaded successfully."
  else
    echo "[ERROR] .env file not found. Exiting..." >&2
    exit 1
  fi
}

# Function to set up the database
setup_database() {
  docker-compose up -d db
  until docker-compose exec db pg_isready; do
    echo "[INFO] Waiting for PostgreSQL to start..."
    sleep 2
  done
  echo "[INFO] PostgreSQL database is available."
  docker-compose exec app alembic upgrade head
  echo "[INFO] Database migrations completed successfully."
}

# Function to start the FastAPI application
start_application() {
  uvicorn api.src.main:app --reload
  echo "[INFO] FastAPI application started successfully."
}

# Main execution block
main() {
  load_environment_variables
  setup_database
  start_application
}

# Entry point for the script
main