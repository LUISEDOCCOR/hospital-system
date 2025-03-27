from flask import render_template

class AdminController ():
    def index(self):
        return render_template("pages/admin/index.html")
