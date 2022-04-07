from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_codespace():
    return "<h2>Hello Codespaces!</h2>"