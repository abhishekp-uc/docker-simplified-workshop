from flask import Flask
server = Flask(__name__)


@server.route("/")
def hello():
    return "<h1>Welcome to the new World!</h1>"


if __name__ == "__main__":
    server.run(debug=True, host='0.0.0.0', port=5000)
