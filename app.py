from flask import Flask, jsonify

app  = Flask(__name__)

@app.route("/marco")
def marco():
    return jsonify({"message": "polo"})


if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 8080)
