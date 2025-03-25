from app import app
from database.config import configure_app
from models.admin_model import AdminModel
import json
from lib.bcrypt import hash_password

db = configure_app()

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        with open("admins.json", "r", encoding="utf-8") as file:
            admins = json.load(file)

        for admin in admins:
            user = AdminModel.query.filter_by(email=admin["email"]).first()
            if not user:
                new_admin = AdminModel(
                    name=admin["name"],
                    cellPhone=admin["cellPhone"],
                    email=admin["email"],
                    password = hash_password(admin["password"])
                )
                db.session.add(new_admin)

        db.session.commit()

    app.run(debug=True, port=4321)
