from flask import Flask, request, jsonify

app = Flask(__name__)

stats = {"likes": 0, "views": 0}

@app.route("/stats", methods=["GET"])
def get_stats():
    return jsonify(stats), 200

@app.route("/stats/like", methods=["POST"])
def add_like():
    stats["likes"] += 1
    return jsonify(stats), 200

@app.route("/stats/view", methods=["POST"])
def add_view():
    stats["views"] += 1
    return jsonify(stats), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)
