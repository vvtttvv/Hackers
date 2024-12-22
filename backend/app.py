from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS

from groq import Groq
import os
import json
from collections import Counter
import re

import requests
from PyPDF2 import PdfReader
from io import BytesIO

import urllib.parse

groq_api_key = os.getenv('GROQ_API_KEY')

groq_client = Groq(api_key=groq_api_key)

with open("./resources/legislation.json", "r") as file:
    docs_list = json.load(file)

# Ensure the loaded data is a list
if isinstance(docs_list, list):
    print("Successfully loaded JSON as a list!")
    # print(docs_list)
else:
    print("The JSON file does not contain a list.")


dummy_invoice_data = [
    {
        "id": 0,
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
    },
    {
        "id": 0,
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
    },
    {
        "id": 0,
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
    },
    {
        "id": 0,
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
    },
    {
        "id": 0,
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
    },
    {
        "id": 0,
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
    },
    {
        "id": 0,
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
    },
    {
        "id": 0,
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
    },
    {
        "id": 0,
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
    },
    {
        "id": 0,
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
    },
    {
        "id": 0,
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
    },
    {
        "id": 0,
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
    },
    {
        "id": 0,
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
    },
    {
        "id": 0,
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
    },
    {
        "id": 0,
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
    },
    {
        "id": 0,
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
    },
    {
        "id": 0,
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
    },
    {
        "id": 0,
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
    },
    {
        "id": 0,
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
    },
    {
        "id": 0,
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
    },
    {
        "id": 0,
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
    },
    {
        "id": 0,
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
    },
    {
        "id": 0,
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
    },
    {
        "id": 0,
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
    },


]


app = Flask(__name__)

CORS(app)


@app.route("/")
def home():
    return "<p>Ho Ho Ho AAAAAAAAAAA</p>"


@app.route("/api/header/")
def header():
    return jsonify("NONE")


@app.route("/api/kiki/")
def kiki():
    resp = groq_chat(request.args.get("q"))
    return resp


@app.route("/api/documents")
def documents():
    return jsonify(dummy_invoice_data)


def groq_chat(q, attachments=None):
    if attachments is None:
        attachments = []
    system_get_todos = """
You are Kiki, a cat mascot.
You speak in a cute 3rd person way.
You ought to summarize the necessary steps for
the user to take based on the given document.
Emphasize and keep important details regarding
to completing the form correctly.
At the same time keep response concise.
Use only English language.
You give each step as a todo task.
"""
    id = get_doc_id_for_question(q)
    print(docs_list[id-1]) if id is not None else print("id: None")
    doc = ""
    url = ""
    if id is not None:
        if "doc" in docs_list[id-1].keys():
            doc = docs_list[id-1]["doc"]
        else:
            url = docs_list[id-1]["instruct"]
            if url is None:
                doc = """
give your best answer based on your knowledge and this form details:\n
""" + get_pdf(docs_list[id-1]["form"])
            else:
                doc = get_pdf(url)
    else:
        doc = """
If this question has something regarding
opening or administrating a srl/business,
guide the user to make his question more specific.
Otherwise, appologyse that answer is impossible,
warn that question might be out of topic.
"""

    if id is None or "form" not in docs_list[id-1].keys() is None:
        system_get_todos="""
You are Kiki, a cat mascot.
You speak in a cute 3rd person way.
You ought to summarize the necessary steps for
the user to take based on the given document.
Emphasize and keep important details.
At the same time keep response concise.
Use only English language.
You give each step as a todo task.
"""

    resp = groq_client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": system_get_todos,
            },
            {
                "role": "user",
                "content": doc + "\nUser question is:\n" + q,
            }
        ],
        model="llama3-8b-8192",
    ).choices[0].message.content

    if id is not None and "form" in docs_list[id-1].keys():
        resp += "\n\nThe form you need to complete: " + urllib.parse.quote(
            docs_list[id-1]["form"][8:]
        ) + " (id: " + str(id) + ")"

    return resp


def get_doc_id_for_question(question, attachments=None):
    if attachments is None:
        attachments = []
    # Tokenize the question into words and extract terms with at least 3 characters
    terms = re.findall(r'\b\w{3,}\b', question.lower())
    matched_ids = []

    # Check each term against the descriptions
    for term in terms:
        matched_ids.extend(
            item["id"] for item in docs_list
            if term in item.get("desc", "").lower()
        )

    phrases_2 = [f"{terms[i]} {terms[i+1]}" for i in range(len(terms) - 1)]
    phrases_3 = [f"{terms[i]} {terms[i+1]} {terms[i+2]}"
                 for i in range(len(terms) - 2)]
    phrases_4 = [
        f"{terms[i]} {terms[i+1]} {terms[i+2]} {terms[i+3]}"
        for i in range(len(terms) - 3)]

    for phrase in phrases_2 + phrases_3 + phrases_4:
        matched_ids.extend(
            item["id"] for item in docs_list
            if phrase in item.get("desc", "").lower()
        )

    for term in terms:
        syllables = re.findall(r'[a-zA-Z]{1,4}', term)
        for i in range(len(syllables)):
            for j in range(i + 1, len(syllables) + 1):
                chunk = " ".join(syllables[i:j])
                matched_ids.extend(
                    item["id"] for item in docs_list
                    if chunk in item.get("desc", "").lower()
                )

    id_counts = Counter(matched_ids)
    print(id_counts)
    most_common = id_counts.most_common()

    if most_common and all(count == most_common[0][1] for _, count in most_common):
        print("huhhhhhhhhh")
        return None

    return most_common[0][0] if most_common else None


def get_pdf(url):
    response = requests.get(url)

    pdf_file = BytesIO(response.content)
    reader = PdfReader(pdf_file)

    text = ""
    for page in reader.pages:
        text += page.extract_text()

    return text


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
