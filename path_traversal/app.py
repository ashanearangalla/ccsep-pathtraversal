import os
from flask import Flask, request, send_file, abort, render_template

app = Flask(__name__)


IMAGE_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), "images"))


PRODUCTS = {
    61: {"name": "Laptop",      "price": "$999.00", "image": "61.jpg",
         "description": "A fast, lightweight laptop for work and study."},
    62: {"name": "Headphones",  "price": "$149.00", "image": "62.jpg",
         "description": "Noise-cancelling over-ear headphones."},
    63: {"name": "Smart Watch", "price": "$249.00", "image": "63.jpg",
         "description": "Tracks fitness and shows notifications."},
}


@app.route("/")
def home():
    return render_template("home.html", products=PRODUCTS)


@app.route("/product")
def product():
    try:
        pid = int(request.args.get("id", ""))
    except ValueError:
        abort(404)

    p = PRODUCTS.get(pid)
    if not p:
        abort(404)

    return render_template("product.html", product=p, pid=pid)


@app.route("/image")
def image():
    filename = request.args.get("filename", "")
    if not filename:
        abort(400)

    path = os.path.join(IMAGE_DIR, filename)

    if not os.path.isfile(path):
        abort(404)

    return send_file(path)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
