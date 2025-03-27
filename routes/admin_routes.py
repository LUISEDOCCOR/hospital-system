from flask import Blueprint
from controllers.admin_controller import AdminController
from decorators.auth_decorator import requires_login, only_admins

bp = Blueprint("admin", __name__, url_prefix="/admin")
adminController = AdminController()

@bp.get("/")
@requires_login
@only_admins
def index ():
    return adminController.index()
