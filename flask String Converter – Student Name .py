from flask import Flask

app = Flask(__name__)

@app.route("/student/<string:name>")
def student(name):
    return "Student Name: " + name

app.run(debug=True)
