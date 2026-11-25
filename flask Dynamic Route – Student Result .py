from flask import Flask

app = Flask(__name__)

@app.route("/student/<name>/<marks>")
def student(name, marks):

    marks = int(marks)

    if marks >= 33:
        result = "Pass"
    else:
        result = "Fail"

    return "Name: " + name + "<br>Result: " + result

app.run(debug=True)
