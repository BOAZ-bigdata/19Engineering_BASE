from flask import Flask
from flask import request, jsonify

app = Flask(__name__)

@app.route("/")
def main():
    message = request.args.get("message")
    return_json = {"message": message}
    return jsonify(return_json)

@app.route("/test")
def test():
    message = request.args.get("message")
    return_json = {"message": message}
    return jsonify(return_json)

if __name__=='__main__':
    app.run(host="0.0.0.0", port=8080)
