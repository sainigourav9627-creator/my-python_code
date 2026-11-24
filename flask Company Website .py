from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Company"

@app.route("/about")
def about():
    return "Company Information"

@app.route("/services")
def services():
    return "Company Services"


@app.route("/employees")
def employees():
    return "Employee Information"

@app.route("/career")
def career():
    return "Job Opportunities"

@app.route("/contact")
def contact():
    return "Contact Information"

app.run (debug = True)
