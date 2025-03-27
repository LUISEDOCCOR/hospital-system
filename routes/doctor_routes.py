from flask import Blueprint
from controllers.doctor_controller import DoctorController
from decorators.auth_decorator import requires_login


bp = Blueprint("doctor", __name__, url_prefix="/doctor")
doctorController = DoctorController()

@bp.get("/")
@requires_login
def index ():
    return doctorController.index()
