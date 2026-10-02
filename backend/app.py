from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>DevOps Cloud Project</title>
        </head>
        <body style="font-family: Arial; text-align: center; margin-top: 100px;">
            <h1>🚀 DevOps Cloud Project</h1>
            <h2>Backend is Running!</h2>
            <p>Version: 1.0</p>
        </body>
    </html>
    """

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "service": "backend"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)