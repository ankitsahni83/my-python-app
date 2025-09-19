from flask import Blueprint
from flask import jsonify

hello_bp = Blueprint("hello", __name__ )

@hello_bp.route("/", methods=["GET"])
def hello():
    return jsonify({"message":"Hello from my-python-app!"})
        