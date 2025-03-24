from flask import Flask, render_template
from routes.doctor_routes import bp as bp_doctor

app = Flask(__name__)
app.register_blueprint(bp_doctor)

@app.get("/ok")
def health_check():
    return "ok"

@app.get("/")
def index():
    return render_template("pages/auth.html")
