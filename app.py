from flask import Flask, render_template
from routes.doctor_routes import bp as bp_doctor
from routes.auth_routes import bp as bp_auth

app = Flask(__name__)
app.register_blueprint(bp_doctor)
app.register_blueprint(bp_auth)

@app.get("/ok")
def health_check():
    return "ok"
