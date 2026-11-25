from flask import Flask

app = Flask(__name__)

@app.route("/about")
def about():
    return "Welcome to About Page"

app.run(debug=True)
