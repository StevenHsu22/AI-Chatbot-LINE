#!/bin/bash

set -o allexport
source .env
set +o allexport

echo "Starting app with PYTHONPATH=$PYTHONPATH"
uvicorn app:app --host 0.0.0.0 --port 8000