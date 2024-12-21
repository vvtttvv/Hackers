from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

dummy_invoice_data = [
    {
        "issued_by": "Lorem Ipsum",
        "issued_on": "ddmmyyyy",
        "due_date": "ddmmyyyy",
        "product": "test product",
        "email": "test@mail.ru",
        "quantity": 69,
        "unit_price": 100,
        "subtotal": 88,
        "tva": 33,
        "total": 76,
        "bank_name": "Xd",
    },
    {
        "issued_by": "Lorem Ipsum",
        "issued_on": "ddmmyyyy",
        "due_date": "ddmmyyyy",
        "product": "test product",
        "email": "test@mail.ru",
        "quantity": 69,
        "unit_price": 100,
        "subtotal": 88,
        "tva": 33,
        "total": 76,
        "bank_name": "Xd",
    },
    {
        "issued_by": "Lorem Ipsum",
        "issued_on": "ddmmyyyy",
        "due_date": "ddmmyyyy",
        "product": "test product",
        "email": "test@mail.ru",
        "quantity": 69,
        "unit_price": 100,
        "subtotal": 88,
        "tva": 33,
        "total": 76,
        "bank_name": "Xd",
    },
    {
        "issued_by": "Lorem Ipsum",
        "issued_on": "ddmmyyyy",
        "due_date": "ddmmyyyy",
        "product": "test product",
        "email": "test@mail.ru",
        "quantity": 69,
        "unit_price": 100,
        "subtotal": 88,
        "tva": 33,
        "total": 76,
        "bank_name": "Xd",
    },
]

dummy_agenda = [
    {
     "id": 0,
     "type": "TODO",
     "content": "lorem ipsum",
     "date": "ddmmyyyy",
     "steps": ["aaaaaaa", "bruh", "step 3", "bruhhhh"],
     },
]


@app.route("/")
def home():
    return "<p>Ho Ho Ho AAAAAAAAAAA</p>"


@app.route("/api/header/")
def header():
    return jsonify("NONE")


@app.route("/api/kiki/")
def agenda():
    resp = groq_chat(request.args.get("q"))
    return resp


@app.route("/api/documents")
def documents():
    return jsonify(dummy_invoice_data)


def groq_chat(q):
    return """
## This is a response from Kiki ><\n
Here are your steps:\n
1. step 1\n
2. one more step\n
3. last step :3\n
""" + q


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
