from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS

from groq import Groq
import os
import json
import imaplib
import email
from collections import Counter
import re

import requests
from PyPDF2 import PdfReader
from io import BytesIO

import urllib.parse

from test import analyze_invoice
import json

load_dotenv()

groq_api_key = os.getenv('GROQ_API_KEY')

groq_client = Groq(api_key=groq_api_key)

endpoint = os.getenv("ENDPOINT")
key = os.getenv("AZURE_KEY")

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

# Directory to save attachments
attachments_dir = 'attachments'
os.makedirs(attachments_dir, exist_ok=True)


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


def documents():
    # Set up the IMAP connection
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login(os.getenv("USERNAME"), os.getenv("PASSWORD"))
    mail.select('inbox')

    # Search for all email messages in the inbox
    status, data = mail.search(None, 'ALL')

    # Process emails
    for num in data[0].split():
        status, data = mail.fetch(num, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_bytes(raw_email, policy=policy.default)
        
        # Check if the subject contains the word 'invoice' (case-insensitive)
        subject = email_message['Subject'] or ""
        if "invoice" in subject.lower():
            has_attachment = False

            # Check if the email is multipart
            if email_message.is_multipart():
                # Iterate through all parts of the email
                for part in email_message.walk():
                    content_disposition = part.get("Content-Disposition", None)
                    if content_disposition and "attachment" in content_disposition:
                        has_attachment = True
                        filename = part.get_filename()
                        if filename:  # If there's an attachment
                            process_attachment(part, filename)  # Process the attachment

            if has_attachment:
                print(f"Email with subject '{subject}' has attachments and contains 'invoice'.")
            else:
                print(f"Email with subject '{subject}' does not have attachments.")
        else:
            print(f"Email with subject '{subject}' skipped (does not contain 'invoice').")
        
    mail.close()
    mail.logout()

    invoices=get_json_files()

    print(invoices)

    return jsonify(invoices)


def process_attachment(part, filename):
    """Save attachment and extract text if applicable."""
    
    # Process PDF files only
    if filename.lower().endswith('.pdf'):  # Check if the file is a PDF first
        # Define the file path for saving the PDF attachment
        file_path = os.path.join(attachments_dir, filename)

        # Check if the file is already in the attachments folder (avoid duplicates)
        if os.path.exists(file_path):
            print(f"File {filename} already exists in attachments. Skipping...")
            return  # Skip processing if the file already exists

        # Save the PDF attachment to the attachments folder
        with open(file_path, 'wb') as f:
            f.write(part.get_payload(decode=True))
        print(f"Saved attachment: {file_path}")

        # Process the saved PDF file for invoice analysis
        print(f"Processing PDF attachment: {filename}")
        analyze_invoice(file_path,endpoint,key)
    else:
        print(f"File {filename} is not a PDF and will not be processed.")



def get_json_files():
    # Directory where JSON files are stored
    json_dir = 'invoices'

    # List to hold all the JSON data
    all_json_data = {}

    # Iterate over all files in the directory
    for filename in os.listdir(json_dir):
        # Only process JSON files
        if filename.endswith('.json'):
            file_path = os.path.join(json_dir, filename)
            
            # Open and load the JSON file content
            with open(file_path, 'r') as json_file:
                try:
                    # Parse the JSON file content
                    file_data = json.load(json_file)
                    # Use the filename (without extension) as the key
                    file_key = os.path.splitext(filename)[0]
                    all_json_data[file_key] = file_data
                except json.JSONDecodeError:
                    print(f"Error decoding JSON from {filename}")
    
    # Return the data as a JSON response
    return all_json_data



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
