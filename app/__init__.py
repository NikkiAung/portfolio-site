import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
from peewee import *
import datetime
from playhouse.shortcuts import model_to_dict
import re

load_dotenv()
app = Flask(__name__)

if os.getenv("TESTING") == "true":
    print("Running in test mode")
    mydb = SqliteDatabase('file:memory?mode=memory&cache=shared', uri=True)
else:
    mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        host=os.getenv("MYSQL_HOST"),
        port=3306
    )

print(mydb)

class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = mydb

mydb.connect()
mydb.create_tables([TimelinePost])


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
    education = [
        {
            "institution": "City College of San Francisco",
            "degree": "BS in Computer Science",
            "duration": "Jan 2024 - Present"
        },
        {
            "institution": "ALBA",
            "degree": "High School Diploma (IGCSE)",
            "duration": "2018 - 2022"
        }
    ]
    return render_template('index.html', education=education, work_experience=work_experience, title="MLH Fellow", url=os.getenv("URL"))


@app.route("/hobbies")
def hobbies():
    hobbies_list = [
        {"name": "Photography", "description": "I enjoy capturing cityscapes and nature scenes.",  "image": "photography.jpg"},
        {"name": "Touching Grass", "description": "I love taking a visit to local garden.", "image": "touching-grass.jpg"},
        {"name": "Hiking", "description": "Exploring trails and being in nature recharges me.", "image": "hiking.jpg"}
    ]
    return render_template("hobbies.html", hobbies=hobbies_list, title="My Hobbies")

@app.route('/timeline')
def timeline():
    return render_template('timeline.html', title="Timeline")


@app.route('/api/timeline_post', methods=['POST'])
def post_time_line_post():
    # Name and content validation
    if not request.form.get('name'):
        return "Invalid name", 400
    
    if not request.form.get('content'):
        return "Invalid content", 400
    
    name = request.form['name']
    content = request.form['content']

    # Email validation
    email = request.form['email']
    regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'
    if not re.match(regex, email):
        return "Invalid email", 400

    timeline_post = TimelinePost.create(name=name, email=email, content=content)
    return model_to_dict(timeline_post)

@app.route('/api/timeline_post', methods=['GET'])
def get_time_line_post():
    return {
        'timeline_posts': [
            model_to_dict(p)
            for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())
        ]
    }

@app.route('/api/timeline_post/<int:post_id>', methods=['DELETE'])
def delete_timeline_post(post_id):
    post = TimelinePost.get_or_none(TimelinePost.id == post_id)
    if post:
        post.delete_instance()
        return {'result': 'deleted'}
    else:
        return {'error': 'Post not found'}, 404
    
