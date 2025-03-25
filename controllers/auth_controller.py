from flask import render_template
from database.extensions import db

class AuthController ():
    def index (self):
        return render_template("pages/auth.html")
