import pytesseract
import re
import json

def extract_data_from_invoice(image_path):
    # Step 1: Perform OCR on the invoice/receipt image
    extracted_text = pytesseract.image_to_string(image_path)

    # Step 2: Parse the extracted text using regular expressions
    invoice_number_match = re.search(r"Invoice No\. (\w+)", extracted_text)
    invoice_number = invoice_number_match.group(1) if invoice_number_match else None

    date_match = re.search(r"Date: (\d{2}/\d{2}/\d{4})", extracted_text)
    date = date_match.group(1) if date_match else None

    total_amount_match = re.search(r"Total: (\d+\.\d{2})", extracted_text)
    total_amount = total_amount_match.group(1) if total_amount_match else None

    # Step 3: Create a data structure
    invoice_data = {
        "invoice_number": invoice_number,
        "date": date,
        "total_amount": total_amount
    }

    # Step 4: Convert data to JSON
    json_data = json.dumps(invoice_data)

    return json_data

# Example usage
invoice_image_path = "files/invoice.png"
json_output = extract_data_from_invoice(invoice_image_path)
print(json_output)
