from models.person_model import PersonModel
from database.extensions import db

class DoctorModel (PersonModel):
    __tablename__ = "doctors"
    id = db.Column(db.Integer, db.ForeignKey('persons.id'), primary_key=True)
    medical_specialty = db.Column(db.String(100), nullable=False)
    __mapper_args__ = {
            'polymorphic_identity': 'doctor'
    }

    def __init__(self, name: str, age: int, cellPhone: int, email: str, gender: str, medical_specialty: str):
        self.medical_specialty = medical_specialty
        super().__init__(name, age, cellPhone, email, gender)
