import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    work_experience = [
        {
            "company": "City College of San Francisco",
            "role": "Lead Full Stack Software Engineer",
            "duration": "Feb 2025 - Jun 2025",
            "description": "Built Zoom automation tools using Electron + React, improving session start times by 99.9%."
        },
        {
            "company": "Mermory",
            "role": "Frontend Developer Intern",
            "duration": "Apr 2025 - May 2025",
            "description": " Partnered with UI/UX designers to translate Figma prototypes into a front-end landing page in code within 2 days"
        }
    ]
    return render_template('index.html', work_experience=work_experience, title="MLH Fellow", url=os.getenv("URL"))
