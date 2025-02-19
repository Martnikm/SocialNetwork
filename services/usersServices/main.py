from flask import Flask, request, jsonify

app = Flask(__name__)

users = []

@app.route("/users", methods=["POST"])
def create_user():
    data = request.json
    user = {"id": len(users) + 1, "username": data["username"], "email": data["email"]}
    users.append(user)
    return jsonify(user), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
