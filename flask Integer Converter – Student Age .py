from flask import Flask

app = Flask(__name__)

@app.route("/age/<int:age>")
def student(age):
    return "Student Age: " + str(age)

app.run(debug=True)
