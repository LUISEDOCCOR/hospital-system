# https://medium.com/@mjpile/setting-up-inheritance-in-sqlalchemy-joined-table-26dd0cb775d8
#https://flask-sqlalchemy.readthedocs.io/en/stable/queries/

from database.extensions import db
from typing import Optional

class PersonModel(db.Model):
    __tablename__ = "persons"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer(), nullable=False)
    cellPhone = db.Column(db.Integer(), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    gender = db.Column(db.String(30), nullable=False)

    type = db.Column(db.String())

    __mapper_args__ = {
            'polymorphic_identity': 'person',
            'polymorphic_on': 'type'
        }

    def __init__(self, name: str, age: int, cellPhone: int, email: str, gender: str):
        self.name = name
        self.age = age
        self.cellPhone = cellPhone
        self.email = email
        self.gender = gender


    def __repr__(self) -> str:
        return f"User: {self.name} | {self.type}"

    @classmethod
    def get_by_id(cls, id: int) -> Optional["PersonModel"]:
        return db.session.execute(db.select(PersonModel).filter_by(id=id)).scalar_one()
