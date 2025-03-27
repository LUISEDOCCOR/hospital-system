from flask import render_template

class DoctorController ():
    def index(self):
        return render_template("pages/doctor/index.html")
