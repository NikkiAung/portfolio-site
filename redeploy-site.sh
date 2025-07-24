#!/bin/bash

# 1. Go to the project directory
cd /portfolio-site || exit

# 2. Make sure we have the latest code from GitHub
git fetch && git reset origin/main --hard

# 3. Clean up any old docker-compose.prod.yml
docker compose -f docker-compose.prod.yml down

# 4. Build the Docker images
docker compose -f docker-compose.prod.yml up -d --build