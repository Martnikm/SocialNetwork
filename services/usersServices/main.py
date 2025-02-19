from flask import Flask, request, jsonify
from database import db_session
from models import User

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    user = User(username=data["username"], email=data["email"], password_hash=data["password"])
    db_session.add(user)
    db_session.commit()
    return jsonify({"message": "User registered successfully"}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
