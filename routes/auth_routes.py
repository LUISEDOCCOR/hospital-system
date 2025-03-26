from flask import Blueprint
from controllers.auth_controller import AuthController

bp = Blueprint("auth", __name__)
authController = AuthController()

@bp.route("/", methods=["POST", "GET"])
def auth ():
    return authController.index()

@bp.get("/admin-panel")
def admin_panel():
    return ""
