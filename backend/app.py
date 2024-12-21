from flask import Flask
from flask import jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return "<p>Wassup</p>"


@app.route("/api/header/")
def header():
    data = {
        "1": "text1",
        "2": "text2"
    }
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)
