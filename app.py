from flask import Flask, jsonify

app  = Flask(__name__)

@app.route("/marco")
def marco():
    return jsonify({"message": "polo"})


if __name__ == "__main__":
    import os
    app.run(host=os.environ.get("FLASK_RUN_HOST", "0.0.0.0"), port=int(os.environ.get("PORT", 8080)))
