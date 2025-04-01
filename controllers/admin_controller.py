from flask import render_template, session, url_for

class AdminController ():

    def global_variables (self):
        return {
            "user_name": session["name"],
            "user_email": session["email"],
            "user_id": session["user_id"],
            "navbar_items": [
                {
                    "icon": "fa-solid fa-notes-medical",
                    "label": "Consultas",
                    "href": url_for("admin.index")
                },
                {
                    "icon": "fa-solid fa-user-doctor",
                    "label": "Doctores",
                    "href": url_for("admin.doctors")
                },
                {
                    "icon": "fa-solid fa-person",
                    "label": "Pacientes",
                    "href": url_for("admin.patients")
                }
            ]
        }

    def index(self):
        return render_template("pages/admin/index.html")

    def doctors(self):
        return render_template("pages/admin/doctors.html")

    def patients(self):
        return render_template("pages/admin/patients.html")
