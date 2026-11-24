from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome page"

@app.route("/salary")
def salary():
    return "Salary Details"

@app.route("/department")
def department():
    return "Department Details"


@app.route("/employees")
def employees():
    return "Employee Details"


@app.route("/report")
def report():
    return "Employee Report"

@app.route("/attendance")
def attendance():
    return "Attendance Details"

app.run (debug = True)
