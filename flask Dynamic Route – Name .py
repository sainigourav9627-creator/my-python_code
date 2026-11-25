from flask import Flask

app = Flask(__name__)

@app.route("/user/<name>")
def user(name):
    return "Welcome " + name

app.run(debug=True)
