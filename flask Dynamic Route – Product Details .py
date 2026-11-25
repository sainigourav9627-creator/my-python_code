from flask import Flask

app = Flask(__name__)

@app.route("/product/<name>/<price>")
def product(name, price):
    return "Product: " + name + "<br>Price: " + price

app.run(debug=True)
