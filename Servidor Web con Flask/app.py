from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Maria Servidor Flask funcionando en Debian!"

@app.route("/ram")
def ram():
    return os.popen("free -h").read()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
