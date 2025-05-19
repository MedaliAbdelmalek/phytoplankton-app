from flask import Blueprint, jsonify
from .models import Utilisateur
from . import db
from uuid import uuid4

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return jsonify(message="API Flask is running with models!")

@main.route('/init-user')
def create_user():
    try:
        user = Utilisateur(
            id=uuid4(),
            nom="Test User",
            email="test@phyto.com",
            mot_de_passe="hashed_password",
            role="UTILISATEUR"
        )
        db.session.add(user)
        db.session.commit()
        return {"message": "Utilisateur ajouté"}
    except Exception as e:
        return {"error": str(e)}, 500
