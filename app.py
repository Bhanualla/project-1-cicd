from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <h1>DevOps Employee Portal</h1>
    <p>Application Version: 1.0</p>
    <p>Status: Running Successfully</p>
    """


@app.route("/health")
def health():
    return {"status": "UP"}, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)