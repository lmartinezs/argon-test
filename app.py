"""ARKON APP"""
import logging
from flask import Flask

logging.basicConfig(filename='flask-access.log', level=logging.DEBUG)

app = Flask(__name__)

POSTS_REQUESTS_FILE = 'post_requests.txt'


@app.route('/count/', methods=['GET'])
def getcount():
    """GET REQUEST"""
    with open(POSTS_REQUESTS_FILE, 'r', encoding="utf-8") as file:
        data = file.read()
    return "Post requests: " + data


@app.route('/count/', methods=['POST'])
def addcount():
    """POST REQUEST."""
    with open(POSTS_REQUESTS_FILE, 'r', encoding="utf-8") as file:
        data = file.read()

    count = str(int(data) + 1)

    with open(POSTS_REQUESTS_FILE, 'w', encoding="utf-8") as file:
        file.write(count)
    return "Post requests: " + count


@app.route("/")
def hello():
    """Welcome to home."""
    return "Hello World!!!"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
