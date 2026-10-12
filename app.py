from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <h1>DevOps Employee Portal</h1>
    <p>Application Version: 1.1</p>
    <p>Status: Running Successfully</p>
    """


@app.route("/health")
def health():
    return {"status": "UP"}, 200


@app.route("/info")
def info():
    return {
        "application": "DevOps Employee Portal",
        "version": "1.1",
        "environment": "development"
    }, 200

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)