#!/bin/bash

# Generate a random string for content
RANDOM_CONTENT="Test post $(date +%s)"

# Create a new timeline post with POST
RESPONSE=$(curl -s -X POST http://127.0.0.1:5000/api/timeline_post \
    -d "name=TestUser&email=test@example.com&content=${RANDOM_CONTENT}")

echo "POST Response:"
echo "$RESPONSE"

# Extracting Post id
POST_ID=$(echo "$RESPONSE" | grep -o '"id":[0-9]*' | grep -o '[0-9]*')

# Get all timeline posts with GET
echo -e "\nGET Response:"
curl -s http://127.0.0.1:5000/api/timeline_post | grep "$RANDOM_CONTENT"

# BONUS: Delete the test post (requires DELETE endpoint: /api/timeline_post/<id>)
if [ -n "$POST_ID" ]; then
    echo -e "\nDeleting test post with ID $POST_ID..."
    curl -s -X DELETE "http://127.0.0.1:5000/api/timeline_post/$POST_ID"
    echo -e "\nDeleted test post."
else
    echo "Could not extract POST ID. Skipping delete."
fi
