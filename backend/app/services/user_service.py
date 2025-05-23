from ..models import Utilisateur, db
from ..utils.auth import hash_password, verify_password, generate_token

def create_user(data):
    if Utilisateur.query.filter_by(email=data['email']).first():
        raise ValueError("Email already exists")
    user = Utilisateur(
        nom=data['nom'],
        email=data['email'],
        mot_de_passe=hash_password(data['mot_de_passe'])
    )
    db.session.add(user)
    db.session.commit()
    return user

def authenticate_user(email, password):
    user = Utilisateur.query.filter_by(email=email).first()
    if not user or not verify_password(password, user.mot_de_passe):
        raise ValueError("Invalid credentials")
    return generate_token(user.id), user

def get_all_users():
    return Utilisateur.query.all()
