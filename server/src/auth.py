from flask import Blueprint, jsonify, request
from src.models import db, Doctor
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, create_refresh_token
import re
from werkzeug.security import generate_password_hash, check_password_hash




auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/login', methods=['POST'])
def login():
    """
    Login a doctor and return a JWT token
    """
    data = request.get_json()
    if not data:
        return jsonify({"error": "No input data provided"}), 400

    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({"error": "Missing email or password"}), 400

    doctor = Doctor.query.filter_by(email=email).first()
    if not doctor or not check_password_hash(doctor.password, password):
        return jsonify({"error": "Invalid credentials"}), 401

    # Create both tokens
    access_token = create_access_token(identity=doctor.id)
    refresh_token = create_refresh_token(identity=doctor.id)
    
    return jsonify({
        "access_token": access_token,
        "refresh_token": refresh_token,
        "identity": doctor.id  
    }), 200


@auth_bp.route('/register', methods=['POST'])
def register():
    """
    Register a new doctor
    """
    data = request.get_json()
    if not data:
        return jsonify({"error": "No input data provided"}), 400

    # Validate required fields
    required_fields = ['fname', 'lname', 'password', 'age', 'email', 'phone', 'topCred']
    missing_fields = [field for field in required_fields if not data.get(field)]
    if missing_fields:
        return jsonify({"error": f"Missing fields: {', '.join(missing_fields)}"}), 400

    # Validate email format
    if not re.match(r"[^@]+@[^@]+\.[^@]+", data['email']):
        return jsonify({"error": "Invalid email format"}), 400

    # Validate password strength
    if len(data['password']) < 8:
        return jsonify({"error": "Password must be at least 8 characters"}), 400

    # Check if email exists
    if Doctor.query.filter_by(email=data['email']).first():
        return jsonify({"error": "Email already registered"}), 400

    # Create doctor
    hashed_password = generate_password_hash(data['password'])
    new_doctor = Doctor(
        fname=data['fname'],
        lname=data['lname'],
        password=hashed_password,
        age=data['age'],
        email=data['email'],
        phone=data['phone'],
        topCred=data['topCred']
    )

    try:
        db.session.add(new_doctor)
        db.session.commit()
        return jsonify(new_doctor.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@auth_bp.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    """
    Logout a doctor
    """
    # Invalidate the token (this can be done by adding it to a blacklist)
    return jsonify({"msg": "Logout successful"}), 200

@auth_bp.route('/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh():
    """
    Refresh a JWT token
    """
    current_user = get_jwt_identity()
    new_token = create_access_token(identity=current_user)
    return jsonify({"access_token": new_token}), 200