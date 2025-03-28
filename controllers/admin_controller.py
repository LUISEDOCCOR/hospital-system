from flask import render_template, session, url_for

class AdminController ():

    def global_variables (self):
        return {
            "user_name": session["name"],
            "user_email": session["email"],
            "user_id": session["user_id"],
            "navbar_items": [
                {
                    "label": "Consultas",
                    "href": url_for("admin.index")
                },
                {
                    "label": "Doctores",
                    "href": url_for("admin.doctors")
                },
                {
                    "label": "Clientes",
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
