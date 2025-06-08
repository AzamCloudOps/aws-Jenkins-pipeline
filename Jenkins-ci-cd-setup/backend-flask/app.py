import logging
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

logging.basicConfig(level=logging.INFO)

@app.route('/')
def home():
    return 'Backend is working auto as tested pipline ', 200

@app.route('/submit', methods=['POST'])
def receive_feedback():
    data = request.get_json()
    app.logger.info(f"Raw JSON received: {data}")
    if not data:
        return {'status': 'error', 'message': 'No JSON received'}, 400

    name = data.get('name')
    email = data.get('email')
    message = data.get('message')

    app.logger.info(f"📩 Feedback received from {name} ({email}): {message}")
    return {'status': 'success'}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)