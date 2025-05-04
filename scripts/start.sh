#!/bin/bash

# Check if .env file exists
if [ ! -f .env ]; then
    echo "Error: .env file not found!"
    echo "Please create .env file from .env.example"
    exit 1
fi

# Start Docker Compose services
docker-compose up -d

echo "LINE LLM Bot service started!"
echo "You can view logs with the following command:"
echo "docker-compose logs -f app"