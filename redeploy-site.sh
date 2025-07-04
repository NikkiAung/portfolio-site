#!/bin/bash

# Kill all existing tmux sessions (to stop any old Flask servers)
tmux kill-server

# Go to the project directory
cd /portfolio-site || exit

# Make sure we have the latest code from GitHub
git fetch
git reset origin/main --hard

# Enter the virtual environment
source python3-virtualenv/bin/activate

# Install any new python dependencies
pip install -r requirements.txt

# Start a new detached tmux session that launches the Flask server
tmux new-session -d -s myporfoliosite "cd /portfolio-site && source python3-virtualenv/bin/activate && flask run --host=0.0.0.0"
