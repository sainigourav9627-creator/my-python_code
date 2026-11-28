from flask import Flask, request

app = Flask(__name__)

@app.route("/employee", methods=["POST"])
def employee():
    name = request.form.get("name")
    return "Employee Name: " + name

app.run(debug=True)
