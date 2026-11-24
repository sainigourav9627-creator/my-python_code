from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome page"

@app.route("/student")
def student():
    return "Student Name"

@app.route("/course")
def course():
    return "Course Name"


@app.route("/result")
def result():
    return "Result Information"

app.run (debug = True)
