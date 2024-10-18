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

# Function to build the Docker image
build_docker_image() {
  docker build -t ai-request-handler:latest .
  echo "[INFO] Docker image built successfully."
}

# Function to push the Docker image to the registry
push_docker_image() {
  docker push ai-request-handler:latest
  echo "[INFO] Docker image pushed successfully."
}

# Function to start the application using Docker Compose
start_application() {
  docker-compose up -d
  echo "[INFO] Application started successfully."
}

# Main execution block
main() {
  load_environment_variables
  build_docker_image
  push_docker_image
  start_application
}

# Entry point for the script
main