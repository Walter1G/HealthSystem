from flask import Blueprint, jsonify, request

from src.models import db, Severity

severity_bp = Blueprint('severity', __name__)

@severity_bp.route('/', methods=['GET'])
def get_severities():
    """
    Get all severities
    """
    severities = Severity.query.all()
    return jsonify({"data":[severity.to_dict() for severity in severities]}), 200

@severity_bp.route('/<int:severity_id>', methods=['GET'])
def get_severity(severity_id):
    """
    Get a severity by ID
    """
    severity = Severity.query.get_or_404(severity_id)
    return jsonify({"data":severity.to_dict()}), 200
    

@severity_bp.route("/<string:title>", methods=["GET"])
def get_severity_by_title(title):
    """
    Get a severity by title
    """
    severity = Severity.query.filter_by(title=title).first()
    if not severity:
        return jsonify({"error": "Severity not found"}), 404
    return jsonify({"data":severity.to_dict()}), 200

@severity_bp.route('/', methods=['POST'])
def create_severity():
    """
    Create a new severity
    """
    data = request.get_json()
    if not data:
        return jsonify({"error": "No input data provided"}), 400

    title = data.get('title')
    description = data.get('description')

    if not title or not description:
        return jsonify({"error": "Missing required fields"}), 400

    new_severity = Severity(title=title, description=description)
    db.session.add(new_severity)
    db.session.commit()

    return jsonify(new_severity.to_dict()), 201

severity_bp.route('/<int:severity_id>', methods=['PUT'])
def update_severity(severity_id):
    """
    Update a severity by ID
    """
    severity = Severity.query.get_or_404(severity_id)
    data = request.get_json()

    if not data:
        return jsonify({"error": "No input data provided"}), 400

    title = data.get('title')
    description = data.get('description')

    if title:
        severity.title = title
    if description:
        severity.description = description

    db.session.commit()
    return jsonify(severity.to_dict()), 200

@severity_bp.route('/<int:severity_id>', methods=['DELETE'])
def delete_severity(severity_id):
    """
    Delete a severity by ID
    """
    severity = Severity.query.get_or_404(severity_id)
    db.session.delete(severity)
    db.session.commit()
    return jsonify({"message": "Severity deleted"}), 200