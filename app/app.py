import os
import socket
from flask import Flask, jsonify

app = Flask(__name__)

CONTAINER_ID = socket.gethostname()


@app.route("/", methods=["GET"])
def index():
    return jsonify({
        "status": "online",
        "service": "LMS Core Application",
        "container_id": CONTAINER_ID,
        "message": "High-Availability LMS Cluster operational"
    }), 200


@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "healthy",
        "container_id": CONTAINER_ID,
        "checks": {
            "web_worker": "running",
            "memory": "optimal"
        }
    }), 200


@app.route("/api/courses", methods=["GET"])
def get_courses():
    courses = [
        {"id": "AWS-101", "name": "AWS Cloud Foundations", "tier": "Associate"},
        {"id": "DOC-201", "name": "Docker & Container Architecture", "tier": "Intermediate"},
        {"id": "LNX-301", "name": "Linux Troubleshooting & RCA", "tier": "Advanced"}
    ]

    return jsonify({
        "container_id": CONTAINER_ID,
        "total_records": len(courses),
        "data": courses
    }), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))
