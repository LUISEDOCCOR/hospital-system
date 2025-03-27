from flask import Flask, render_template
from routes.doctor_routes import bp as bp_doctor
from routes.auth_routes import bp as bp_auth
from routes.admin_routes import bp as bp_admin
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("secret_key")

app.register_blueprint(bp_doctor)
app.register_blueprint(bp_auth)
app.register_blueprint(bp_admin)

@app.get("/ok")
def health_check():
    return "ok"
