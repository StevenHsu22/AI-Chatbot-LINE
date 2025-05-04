#!/bin/sh

# Check if .env file exists
# if [ ! -f .env ]; then
#     echo "Error: .env file not found!"
#     echo "Please create .env file from .env.example"
#     exit 1
# fi

echo "Starting FastAPI server..."
uvicorn app:app --host 0.0.0.0 --port 8000