from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeResult
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest
from dotenv import load_dotenv
import os
import json
from pathlib import Path



def analyze_invoice(filepath, endpoint, key):
    # sample document

    client = DocumentIntelligenceClient(
        endpoint=endpoint, credential=AzureKeyCredential(key)
    )
    with open(filepath, 'rb') as file:
        file_content = file.read()

    poller = client.begin_analyze_document(
        "prebuilt-invoice",
        AnalyzeDocumentRequest(bytes_source=file_content)
    )
    data = {}
    invoices = poller.result()
    if invoices.documents:
        for idx, invoice in enumerate(invoices.documents):
            vendor_name = invoice.fields.get("VendorName")
            if vendor_name:
                data["issued_by"] = vendor_name.get('content')

            invoice_date = invoice.fields.get("InvoiceDate")
            if invoice_date:
                data["issued_on"] = invoice_date.get('content')

            due_date = invoice.fields.get("DueDate")
            if due_date:
                data["due_date"] = due_date.get('content')

  
            for idx, item in enumerate(invoice.fields.get("Items").get("valueArray")):

                item_description = item.get("valueObject").get("Description")
                if item_description:
                    data["product"] = item_description.get('content')
                item_quantity = item.get("valueObject").get("Quantity")
                if item_quantity:
                    data["quantity"]=item_quantity.get('content')
                unit_price = item.get("valueObject").get("Amount")
                if unit_price:
                    data["unit_price"] = unit_price.get('content')
                

            subtotal = invoice.fields.get("SubTotal")
            if subtotal:
                data["subtotal"] = subtotal.get('content')

            total_tax = invoice.fields.get("TotalTax")
            if total_tax:
                data["tva"] = total_tax.get('content')

            amount_due = invoice.fields.get("AmountDue")
            if amount_due:
                data["total"] = amount_due.get('content')
            

    
    file_path = os.path.join("invoices", Path(os.path.basename(filepath)).stem + '.json')
    data["url"] = filepath

    # Write the dictionary to a data file
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)
                
            
           
            
            
            




# analyze_invoice('attachments/invoice-1.pdf')