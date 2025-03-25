from models.person_model import PersonModel
from database.extensions import db
import bcrypt

class AdminModel (PersonModel):
    __tablename__ = "admins"
    id = db.Column(db.Integer, db.ForeignKey('persons.id'), primary_key=True)
    password = db.Column(db.String(255), nullable=False)
    __mapper_args__ = {
            'polymorphic_identity': 'admin'
    }

    def __init__(self, name: str, cellPhone: int, email: str, password:str):
        self.password = password
        super().__init__(
            name=name,
            cellPhone=cellPhone,
            email=email,
            gender="admin",
            age=0
        )

    def verify_password (self, password):
        return bcrypt.checkpw(password.encode("utf-8"),self.password.encode("utf-8"))
