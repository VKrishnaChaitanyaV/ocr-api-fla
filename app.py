from flask import Flask, request, jsonify
import pytesseract
from PIL import Image
import base64
import io
import os

app = Flask(__name__)

@app.route('/extract-text', methods=['POST'])
def extract_text():
    data = request.get_json()

    if 'image_base64' not in data:
        return jsonify({'error': 'Missing image_base64'}), 400

    try:
        base64_str = data.get("image_base64")
        if "," in base64_str:
            base64_str = base64_str.split(",")[1]
        # Decode the image
        image_data = base64.b64decode(data['image_base64'])
        image = Image.open(io.BytesIO(image_data))

        # OCR with Tesseract
        text = pytesseract.image_to_string(image)

        return jsonify({'text': text})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))  # Render assigns the PORT dynamically
    app.run(host='0.0.0.0', port=port)
