from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def ocrget():
    return jsonify({'results': 'Get Api v1'})

if __name__ == '__main__':
    app.run(debug=True)

