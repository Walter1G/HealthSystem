from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

db = SQLAlchemy()

# This is a mixin class that provides a method to convert the model instance to a dictionary.


class SerializerMixin:
    __exclude__ = []

    def to_dict(self):
        return {
            column.name: getattr(self, column.name)
            for column in self.__table__.columns
            if column.name not in getattr(self, '__exclude__', [])
        }


# Join Table for many-to-many relationship between Patient and HealthProgram
patient_programs = db.Table(
    'patientPrograms',
    db.Column('patient_id', db.Integer, db.ForeignKey(
        'patients.id'), primary_key=True),
    db.Column('program_id', db.Integer, db.ForeignKey(
        'healthPrograms.id'), primary_key=True),
    db.Column('createdAt', db.DateTime, server_default=func.now()),
    db.Column('updatedAt', db.DateTime, onupdate=func.now())
)

# This is the model for the severity table
# It contains the severity levels for health programs


class Severity(db.Model, SerializerMixin):
    __tablename__ = "severity"

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    title = db.Column(db.String(8), nullable=False)
    description = db.Column(db.String(120))
    createdAt = db.Column(db.DateTime, server_default=func.now())
    updatedAt = db.Column(db.DateTime, onupdate=func.now())

    def __repr__(self):
        return f"<Severity {self.title}>"


# This is the model for the health programs table
# It contains the health programs that can be assigned to patients
class HealthProgram(db.Model, SerializerMixin):
    __tablename__ = "healthPrograms"

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text, nullable=False)
    severity = db.Column(db.Integer, db.ForeignKey('severity.id'))
    createdAt = db.Column(db.DateTime, server_default=func.now())
    updatedAt = db.Column(db.DateTime, onupdate=func.now())

    patients = db.relationship(
        "Patient",
        secondary=patient_programs,
        back_populates="healthPrograms",
        lazy=True
    )

    def __repr__(self):
        return f"<HealthProgram {self.title}>"


class Patient(db.Model, SerializerMixin):
    __tablename__ = "patients"

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    fname = db.Column(db.String(80), nullable=False)
    lname = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(15), unique=True, nullable=False)
    address = db.Column(db.String(120), nullable=False)
    createdAt = db.Column(db.DateTime, server_default=func.now())
    updatedAt = db.Column(db.DateTime, onupdate=func.now())

    healthPrograms = db.relationship(
        "HealthProgram",
        secondary=patient_programs,
        back_populates="patients",
        lazy=True
    )

    def __repr__(self):
        return f"<Patient {self.fname} {self.lname}>"


# This is the model for the doctors table
# It contains the doctors that can Manage patients using the system
class Doctor(db.Model, SerializerMixin):
    __tablename__ = "doctors"

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    fname = db.Column(db.String(80), nullable=False)
    lname = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(15), unique=True, nullable=False)
    topCred = db.Column(db.String(120), nullable=False)
    createdAt = db.Column(db.DateTime, server_default=func.now())
    updatedAt = db.Column(db.DateTime, onupdate=func.now())

    def __repr__(self):
        return f"<Doctor {self.fname} {self.lname}>"
