from flask import Flask

app = Flask(__name__)

@app.route("/student/<int:id>")
def student(id):
    return "Student ID: " + str(id)

app.run(debug=True)
