from flask import Flask, render_template, request
import os
import pytesseract
import re
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    # Get the uploaded file
    file = request.files['file']

    # Save the file to a temporary location
    file_path = os.path.join('uploads', file.filename)
    file.save(file_path)

    # Process the uploaded file
    json_output = extract_data_from_invoice(file_path)

    # Remove the temporary file
    os.remove(file_path)

    return json_output

def extract_data_from_invoice(image_path):
    # Same code as before...

if __name__ == '__main__':
    app.run()