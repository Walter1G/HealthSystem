from flask import Blueprint, jsonify, request
from src.models import db, Patient


patients_bp = Blueprint('patients', __name__)

@patients_bp.route('/', methods=['GET'])
def get_patients():
    """
    Get all patients
    """
    patients = Patient.query.all()
    return jsonify({"data":[patient.to_dict() for patient in patients]}), 200

@patients_bp.route('/<int:patient_id>', methods=['GET'])
def get_patient(patient_id):
    """
    Get a patient by ID
    """
    patient = Patient.query.get_or_404(patient_id)
    return jsonify({"data":patient.to_dict()}), 200

@patients_bp.route('/', methods=['POST'])
def create_patient():
    """
    Create a new patient
    """
    data = request.get_json()
    if not data:
        return jsonify({"error": "No input data provided"}), 400

    fname = data.get('fname')
    lname = data.get('lname')
   
    age = data.get('age')
    email = data.get('email')
    phone = data.get('phone')
    address = data.get('address')

    if not fname or not lname  or not age or not email or not phone or not address:
        return jsonify({"error": "Missing required fields"}), 400
    
    # Check if email already exists
    existing_email = Patient.query.filter_by(email=email).first()
    if existing_email:
        return jsonify({"error": "Email already exists"}), 400
    
    # Check if phone already exists
    existing_phone = Patient.query.filter_by(phone=phone).first()
    if existing_phone:
        return jsonify({"error": "Phone number already exists"}), 400

    new_patient = Patient(fname=fname, lname=lname,  age=age, email=email, phone=phone, address=address)
    db.session.add(new_patient)
    db.session.commit()

    return jsonify({"data":new_patient.to_dict()}), 201


@patients_bp.route('/<int:patient_id>', methods=['PUT'])
def update_patient(patient_id):
    """
    Update a patient by ID
    """
    patient = Patient.query.get_or_404(patient_id)
    data = request.get_json()

    # If email is being changed
    if "email" in data and data["email"] != patient.email:
        existing = Patient.query.filter_by(email=data["email"]).first()
        if existing:
            return jsonify({"error": "Email already exists"}), 400

    # If phone is being changed
    if "phone" in data and data["phone"] != patient.phone:
        existing = Patient.query.filter_by(phone=data["phone"]).first()
        if existing:
            return jsonify({"error": "Phone number already exists"}), 400

    for key, value in data.items():
        setattr(patient, key, value)

    db.session.commit()
    return jsonify({"data":patient.to_dict()}), 200


@patients_bp.route('/<int:patient_id>', methods=['DELETE'])
def delete_patient(patient_id):
    """
    Delete a patient by ID
    """
    patient = Patient.query.get_or_404(patient_id)
    db.session.delete(patient)
    db.session.commit()
    return jsonify({"message": "Patient deleted successfully"}), 200
