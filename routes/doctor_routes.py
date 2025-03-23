from flask import Blueprint
from controllers.doctor_controller import DoctorController

bp = Blueprint("doctor", __name__, url_prefix="/doctor")
doctorController = DoctorController()

@bp.get("/")
def index ():
    return doctorController.getAll()
