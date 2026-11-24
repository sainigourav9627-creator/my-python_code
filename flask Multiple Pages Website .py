from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "home page"

@app.route("/about")
def about():
    return "about page"

@app.route("/service")
def service():
    return "Service page"


@app.route("/contact")
def contact():
    return "Contact page"

app.run (debug = True)
