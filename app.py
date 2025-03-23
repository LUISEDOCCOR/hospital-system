from flask import Flask
from routes.doctor_routes import bp as bp_doctor

app = Flask(__name__)
app.register_blueprint(bp_doctor)

@app.get("/ok")
def health_check():
    return "ok"
