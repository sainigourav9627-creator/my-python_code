from flask import Flask

app = Flask(__name__)

@app.route("/product/<float:price>")
def product(price):
    return "Product Price: " + str(price)

app.run(debug=True)
