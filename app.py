from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def ocrget():
    # You can also add additional logging or error handling if needed
    try:
        return jsonify({'results': 'Get Api v1'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
