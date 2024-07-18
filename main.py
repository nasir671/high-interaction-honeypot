from flask import Flask, request, send_from_directory
import logging
import os

app = Flask(__name__)

# Configure logging
logging.basicConfig(filename='honeypot.log', level=logging.INFO,
                    format='%(asctime)s %(message)s')

# Route to capture all requests
@app.route('/', defaults={'path': ''})
@app.route('/index')
def catch_all(path):
    attacker_ip = request.remote_addr
    method = request.method
    full_path = request.full_path

    # Log the attacker's details
    logging.info(f"IP: {attacker_ip} Method: {method} Path: {full_path}")

    # Respond to the attacker
    return "This is a honeypot. Your activity has been logged.", 200

# Route to capture additional data (e.g., headers, POST data)
@app.route('/capture', methods=['POST'])
def capture_data():
    attacker_ip = request.remote_addr
    headers = request.headers
    data = request.data

    # Log the attacker's details and data
    logging.info(f"IP: {attacker_ip} Headers: {headers} Data: {data}")

    return "Data captured.", 200

# Route to handle file uploads (for malware capture)
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part", 400
    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400
    file.save(os.path.join(UPLOAD_FOLDER, file.filename))

    attacker_ip = request.remote_addr
    logging.info(f"IP: {attacker_ip} uploaded file: {file.filename}")

    return "File uploaded.", 200

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == '__main__':
    app.run(host='localhost', port=5555)
