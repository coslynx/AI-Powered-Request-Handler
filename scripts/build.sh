#!/bin/bash

# Function to format code using black
format_code() {
  black .
}

# Function to lint code using flake8
lint_code() {
  flake8 .
}

# Function to run unit tests using pytest
run_tests() {
  pytest
}

# Function to build the Docker image
build_docker_image() {
  # Optional optimization: Check if image is already built
  # If not built:
  #   format_code
  #   lint_code
  #   run_tests
  docker build -t ai-request-handler:latest .
}

# Load environment variables from .env
if [ -f .env ]; then
  source .env
fi

# Build the Docker image
build_docker_image