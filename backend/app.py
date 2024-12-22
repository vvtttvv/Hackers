from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import imaplib
import email
from email import policy
import os
from PyPDF2 import PdfReader
from docx import Document
from PIL import Image
import pytesseract
from dotenv import load_dotenv


app = Flask(__name__)

CORS(app)

# Load environment variables from the .env file
load_dotenv()

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

    return jsonify(dummy_invoice_data)


# Directory to save attachments
attachments_dir = 'attachments'
os.makedirs(attachments_dir, exist_ok=True)

def extract_text_from_pdf(file_path):
    """Extract text from a PDF file."""
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def extract_text_from_docx(file_path):
    """Extract text from a Word document."""
    doc = Document(file_path)
    return '\n'.join([p.text for p in doc.paragraphs])

def extract_text_from_image(file_path):
    """Extract text from an image using Tesseract."""
    image = Image.open(file_path)
    return pytesseract.image_to_string(image)

def process_attachment(part, filename):
    """Save attachment and extract text if applicable."""
    file_path = os.path.join(attachments_dir, filename)
    with open(file_path, 'wb') as f:
        f.write(part.get_payload(decode=True))
    print(f"Saved attachment: {file_path}")
    
    # Extract text based on file type
    if filename.endswith('.pdf'):
        print("Extracted text from PDF:")
        print(extract_text_from_pdf(file_path))
    elif filename.endswith('.docx'):
        print("Extracted text from Word document:")
        print(extract_text_from_docx(file_path))
    elif filename.endswith(('.png', '.jpg', '.jpeg')):
        print("Extracted text from image:")
        print(extract_text_from_image(file_path))
    else:
        print("File type not supported for text extraction.")



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



    
