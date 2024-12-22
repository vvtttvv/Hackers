from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import imaplib
import email
from email import policy
import os
from dotenv import load_dotenv
from test import analyze_invoice
import json


app = Flask(__name__)

CORS(app)

# Load environment variables from the .env file
load_dotenv()

endpoint = os.getenv("ENDPOINT")
key = os.getenv("AZURE_KEY")


# Directory to save attachments
attachments_dir = 'attachments'
os.makedirs(attachments_dir, exist_ok=True)


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



    
