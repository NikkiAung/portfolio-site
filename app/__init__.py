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


@app.route("/hobbies")
def hobbies():
    hobbies_list = [
        {"name": "Photography", "description": "I enjoy capturing cityscapes and nature scenes."},
        {"name": "Touching Grass", "description": "I love taking a visit to local garden."},
        {"name": "Hiking", "description": "Exploring trails and being in nature recharges me."}
    ]
    return render_template("hobbies.html", hobbies=hobbies_list, title="My Hobbies")
