from flask import Flask

app = Flask(__name__)

@app.route("/file/<path:file_path>")
def student(file_path):
    return "File Path: " + file_path

app.run(debug=True)
