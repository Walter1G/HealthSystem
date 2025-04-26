from flask import Blueprint, jsonify, request
from src.models import db, Doctor


doctors_bp = Blueprint('doctors', __name__)


@doctors_bp.route('/', methods=['GET'])
def get_doctors():
    """
    Get all doctors
    """
    doctors = Doctor.query.all()
    return jsonify([doctor.to_dict() for doctor in doctors]), 200


@doctors_bp.route('/<int:doctor_id>', methods=['GET'])
def get_doctor(doctor_id):
    """
    Get a doctor by ID
    """
    doctor = Doctor.query.get_or_404(doctor_id)
    return jsonify(doctor.to_dict()), 200


@doctors_bp.route('/', methods=['POST'])
def create_doctor():
    """
    Create a new doctor
    """
   
    data = request.get_json()
    new_doctor = Doctor(
        fname=data['fname'],
        lname=data['lname'],
        password=data['password'],
        age=data['age'],
        email=data['email'],
        phone=data['phone'],
        topCred=data['topCred']
    )
    db.session.add(new_doctor)
    db.session.commit()
    return jsonify(new_doctor.to_dict()), 201


@doctors_bp.route('/<int:doctor_id>', methods=['PUT'])
def update_doctor(doctor_id):
    """
    Update a doctor by ID
    """
    doctor = Doctor.query.get_or_404(id)
    data = request.get_json()

    # If email is being changed
    if "email" in data and data["email"] != doctor.email:
        existing = Doctor.query.filter_by(email=data["email"]).first()
        if existing:
            return jsonify({"error": "Email already exists"}), 400

    # If phone is being changed
    if "phone" in data and data["phone"] != doctor.phone:
        existing = Doctor.query.filter_by(phone=data["phone"]).first()
        if existing:
            return jsonify({"error": "Phone number already exists"}), 400

    
    allowed_fields = ["fname", "lname", "password", "age", "email", "phone", "topCred"]
    for field in allowed_fields:
        if field in data:
            setattr(doctor, field, data[field])

    db.session.commit()

    return jsonify(doctor.to_dict()), 200


@doctors_bp.route('/<int:doctor_id>', methods=['DELETE'])
def delete_doctor(doctor_id):
    """
    Delete a doctor by ID
    """
    doctor = Doctor.query.get_or_404(doctor_id)
    db.session.delete(doctor)
    db.session.commit()
    return jsonify({'message': 'Doctor deleted successfully'}), 200
