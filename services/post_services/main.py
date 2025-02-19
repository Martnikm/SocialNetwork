from flask import Flask, request, jsonify

app = Flask(__name__)

posts = []

@app.route("/posts", methods=["POST"])
def create_post():
    data = request.json
    post = {"id": len(posts) + 1, "user_id": data["user_id"], "content": data["content"]}
    posts.append(post)
    return jsonify(post), 201

@app.route("/posts", methods=["GET"])
def get_posts():
    return jsonify(posts), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
