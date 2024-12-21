from flask import Flask
from flask import jsonify

app = Flask(__name__)

dummy_data = [
    {
        "issued_by": "Lorem Ipsum",
        "issued_on": "ddmmyyyy",
        "due_date": "ddmmyyyy",
        "product": "test product",
        "quantity": 69,
        "unit_price": 100,
        "subtotal": 88,
        "tva": 33,
        "total": 76,
        "bank_name": "Xd",
    }
]


@app.route("/")
def home():
    return "<p>Wassup</p>"


@app.route("/api/header/")
def header():
    return jsonify(dummy_data)


if __name__ == "__main__":
    app.run(debug=True)
