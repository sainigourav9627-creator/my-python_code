from flask import Flask

app = Flask(__name__)

@app.route("/employee", methods=["GET"])
def employee():
    return "Employee Name: " + "Department"

app.run(debug=True)
