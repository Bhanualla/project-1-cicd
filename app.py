import os

from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <h1>DevOps Employee Portal</h1>
    <p>Application Version: 1.2</p>
    <p>Status: Running Successfully</p>
    <p>Deployment: Docker Container</p>
    """


@app.route("/health")
def health():
    return {"status": "UP"}, 200


@app.route("/info")
def info():
    return {
        "application": "DevOps Employee Portal",
        "version": "1.2",
        "environment": "development"
    }, 200

if __name__ == "__main__":
    host = os.environ.get("FLASK_HOST", "127.0.0.1")
    app.run(host=host, port=5000)