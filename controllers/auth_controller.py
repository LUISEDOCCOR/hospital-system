from flask import render_template, flash, request, redirect, session
from flask.helpers import url_for
from models.admin_model import AdminModel

class AuthController ():
    def index (self):
        """
        Este método verifica las claves (correo y contraseña)
        del usuario que intenta ingresar y, dependiendo si es
        doctor o administrador, lo manda a la página
        correspondiente
        """

        if request.method == "POST":
            email = request.form.get("email")
            password = request.form.get("password")

            user = AdminModel.get_by_email(email)

            if not user:
                flash("No existe ese correo")
                return render_template("pages/auth.html")

            if not user.verify_password(password):
                flash("Contraseña incorrecta")
                return render_template("pages/auth.html")

            session["name"] = user.name
            session["email"] = user.email
            session["user_id"] = user.id

            if user.type == "admin":
                return redirect(url_for("admin.index"))
            else:
                return redirect(url_for("doctor.index"))

        return render_template("pages/auth.html")

    def logout (self):
        session.clear()
        return  redirect(url_for("auth.index"))
