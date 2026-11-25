from flask import Flask

app = Flask(__name__)

@app.route("/employee/<name>/<city>")
def employee(name, city):
    return name + " " + city

app.run(debug=True)
