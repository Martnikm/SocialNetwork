from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

USER_SERVICE_URL = "http://users_service:5001"
POSTS_SERVICE_URL = "http://posts_service:5002"
STATS_SERVICE_URL = "http://stats_service:5003"

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    response = requests.post(f"{USER_SERVICE_URL}/register", json=data)
    return jsonify(response.json())

@app.route('/posts', methods=['GET'])
def get_posts():
    response = requests.get(f"{POSTS_SERVICE_URL}/posts")
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
