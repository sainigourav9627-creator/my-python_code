from flask import Flask

app = Flask(__name__)

@app.route("/employee/<name>/<salary>")
def employee(name, salary):

    salary = int(salary)

    if salary >= 15000:
        result = "Eligible"

    elif salary >= 10000:
        result = "Waiting"

    else:
        result = "Not Eligible"

    return "Name: " + name + "<br>Status: " + result

app.run(debug=True)
