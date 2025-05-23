# from flask import Blueprint, request, jsonify
# from werkzeug.security import generate_password_hash, check_password_hash
# from .models import Utilisateur
# from . import db
# from uuid import uuid4

# main = Blueprint('main', __name__)

# @main.route('/')
# def index():
#     return jsonify(message="API Flask is running with models!")

# # ✅ Route : SIGNUP
# @main.route('/signup', methods=['POST'])
# def signup():
#     try:
#         data = request.get_json()

#         nom = data.get("nom")
#         email = data.get("email")
#         mot_de_passe = data.get("mot_de_passe")

#         if not nom or not email or not mot_de_passe:
#             return jsonify(error="Tous les champs sont requis"), 400

#         # Vérifier si l'utilisateur existe déjà
#         if Utilisateur.query.filter_by(email=email).first():
#             return jsonify(error="Email déjà utilisé"), 400

#         # Créer un nouvel utilisateur
#         utilisateur = Utilisateur(
#             id=uuid4(),
#             nom=nom,
#             email=email,
#             mot_de_passe=generate_password_hash(mot_de_passe),
#             role="UTILISATEUR"
#         )
#         db.session.add(utilisateur)
#         db.session.commit()

#         return jsonify(message="Inscription réussie"), 201

#     except Exception as e:
#         return jsonify(error=str(e)), 500

# # ✅ Route : SIGNIN
# @main.route('/signin', methods=['POST'])
# def signin():
#     try:
#         data = request.get_json()

#         email = data.get("email")
#         mot_de_passe = data.get("mot_de_passe")

#         if not email or not mot_de_passe:
#             return jsonify(error="Email et mot de passe requis"), 400

#         user = Utilisateur.query.filter_by(email=email).first()

#         if not user or not check_password_hash(user.mot_de_passe, mot_de_passe):
#             return jsonify(error="Identifiants invalides"), 401

#         # Retourner les infos essentielles (tu peux personnaliser selon ton besoin)
#         return jsonify({
#             "id": str(user.id),
#             "nom": user.nom,
#             "email": user.email,
#             "role": user.role
#         }), 200

#     except Exception as e:
#         return jsonify(error=str(e)), 500
