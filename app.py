from flask import Flask, request, jsonify
import easyocr
import numpy as np
import cv2
import base64

app = Flask(__name__)

# Initialize EasyOCR reader
reader = easyocr.Reader(['en'])  # Add other languages if needed

@app.route('/ocrget', methods=['GET'])
def ocrget():
    return jsonify({'results': 'Get Api v1'})

@app.route('/ocr-base64', methods=['POST'])
def ocr_base64():
    data = request.get_json()

    if not data or 'image_base64' not in data:
        return jsonify({'error': 'Missing image_base64 in request'}), 400

    try:
        # Decode base64 string to bytes
        image_data = base64.b64decode(data['image_base64'])
        
        # Convert bytes to numpy array and decode to OpenCV image
        nparr = np.frombuffer(image_data, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        # Run OCR
        results = reader.readtext(img)
        restext = []
        for bbox, text, conf in results:
            restext.append(text)

        return jsonify({'results': restext})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

