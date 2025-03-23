import os
from app import app
from database.extensions import db

basedir = os.path.abspath(os.path.dirname(__file__))

def configure_app ():
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{os.path.join(basedir, 'database.db')}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    return db
