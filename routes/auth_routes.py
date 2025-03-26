from flask import Blueprint
from controllers.auth_controller import AuthController

bp = Blueprint("auth", __name__)
authController = AuthController()

@bp.route("/", methods=["POST", "GET"])
def index ():
    return authController.index()
