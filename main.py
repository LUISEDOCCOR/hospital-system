from app import app
from database.config import configure_app

db = configure_app()

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
