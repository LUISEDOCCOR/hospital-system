from flask import Blueprint
from controllers.admin_controller import AdminController
from decorators.auth_decorator import requires_login, only_admins

bp = Blueprint("admin", __name__, url_prefix="/admin")
adminController = AdminController()

@bp.context_processor
def global_variables():
    return adminController.global_variables()


@bp.get("/")
@requires_login
@only_admins
def index ():
    return adminController.index()

@bp.get("/doctors")
@requires_login
@only_admins
def doctors ():
    return adminController.doctors()

@bp.get("/patients")
@requires_login
@only_admins
def patients ():
    return adminController.patients()
