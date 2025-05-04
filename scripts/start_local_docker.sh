#!/bin/bash

# Check if .env file exists
if [ ! -f .env ]; then
    echo "Error: .env file not found!"
    echo "Please create .env file from .env.example"
    exit 1
fi

echo "Starting docker compose..."
docker compose up -d