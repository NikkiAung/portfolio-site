#!/bin/bash

# 1. Go to the project directory
cd /portfolio-site || exit

# 2. Make sure we have the latest code from GitHub
git fetch
git reset origin/main --hard

# 3. Enter the virtual environment
source python3-virtualenv/bin/activate

# 4. Install any new python dependencies
pip install -r requirements.txt

# 5. Restart the systemd service (replace 'myportfolio' with your actual service name if different)
sudo systemctl restart my-portfolio

echo "Site redeployed and service restarted! :)"
