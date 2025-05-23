from flask import Blueprint, jsonify

main_bp = Blueprint('main', __name__)

@main_bp.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Phytoplancton Backend is running"}), 200

@main_bp.route('/favicon.ico')
def favicon():
    return '', 204 
