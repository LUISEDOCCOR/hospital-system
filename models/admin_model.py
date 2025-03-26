from models.person_model import PersonModel
from database.extensions import db
from lib.bcrypt import hashpw, checkpw
from typing import Optional

class AdminModel (PersonModel):
    __tablename__ = "admins"
    id = db.Column(db.Integer, db.ForeignKey('persons.id'), primary_key=True)
    password = db.Column(db.String(255), nullable=False)
    __mapper_args__ = {
            'polymorphic_identity': 'admin'
    }

    def __init__(self, name: str, cellPhone: int, email: str, password:str):
        self.password = hashpw(password)
        super().__init__(
            name=name,
            cellPhone=cellPhone,
            email=email,
            gender="admin",
            age=0
        )

    def verify_password (self, password):
        """
        Verifica si la contraseña proporcionada coincide
        con la contraseña almacenada.
        """
        return checkpw(password, self.password)

    @classmethod
    def get_by_email (cls, email) -> Optional["AdminModel"]:
        """
        Busca un administrador por su dirección
        de correo electrónico.
        """
        return db.session.execute(db.select(AdminModel).filter_by(email=email)).scalar_one_or_none()
