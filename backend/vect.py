from vlite import VLite

import requests
from PyPDF2 import PdfReader
from io import BytesIO


def get_pdf(url):
    response = requests.get(url)

    pdf_file = BytesIO(response.content)
    reader = PdfReader(pdf_file)

    text = ""
    for page in reader.pages:
        text += page.extract_text()

    return text


vdb = VLite()
vdb.add("hello world", metadata={"artist": "adele"})
vdb.add(get_pdf("https://sfs.md/uploads/document/234/document/ghidul-contribuabilului-incepator-66daa054eb6df.pdf"))

results = vdb.retrieve("how do transformers work?")
print(results)
