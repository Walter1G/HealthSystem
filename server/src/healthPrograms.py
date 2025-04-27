from flask import Blueprint, jsonify, request
from src.models import db, HealthProgram, Severity


health_programs_bp = Blueprint('health_programs', __name__)


@health_programs_bp.route('/', methods=['GET'])
def get_health_programs():
    """
    Get all health programs
    """
    health_programs = HealthProgram.query.all()
    return jsonify({"data":[program.to_dict() for program in health_programs]}), 200

@health_programs_bp.route('/<int:program_id>', methods=['GET'])
def get_health_program(program_id):
    """
    Get a health program by ID
    """
    health_program = HealthProgram.query.get_or_404(program_id)
    return jsonify({"data":health_program.to_dict()}), 200

@health_programs_bp.route('/', methods=['POST'])
def create_health_program():
    """
    Create a new health program
    """
    data = request.get_json()
    if not data:
        return jsonify({"error": "No input data provided"}), 400

    title = data.get('title')
    description = data.get('description')
    severityId = data.get('severity')
   
   

    if not title or not description or not severityId:
        return jsonify({"error": "Missing required fields"}), 400
     

    severity = Severity.query.get_or_404(severityId)


    new_program = HealthProgram(title=title, description=description, severity=severityId)
    db.session.add(new_program)
    db.session.commit()

    return jsonify({"data":new_program.to_dict()}), 201

@health_programs_bp.route('/<int:program_id>', methods=['PUT'])
def update_health_program(program_id):
    """
    Update a health program by ID
    """
    health_program = HealthProgram.query.get_or_404(program_id)
    data = request.get_json()

    # If severity is being changed
    if "severity" in data and data["severity"] != health_program.severity:
        existing = Severity.query.filter_by(id=data["severity"]).first()
        if not existing:
            return jsonify({"error": "Severity not found"}), 404

    # Update the health program fields
    for key, value in data.items():
        setattr(health_program, key, value)

    db.session.commit()
    return jsonify({"data":health_program.to_dict()}), 200

@health_programs_bp.route('/<int:program_id>', methods=['DELETE'])
def delete_health_program(program_id):
    """
    Delete a health program by ID
    """
    health_program = HealthProgram.query.get_or_404(program_id)
    db.session.delete(health_program)
    db.session.commit()
    return jsonify({"message": "Health program deleted successfully"}), 200
