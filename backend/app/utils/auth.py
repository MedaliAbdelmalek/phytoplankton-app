from werkzeug.security import generate_password_hash, check_password_hash
import jwt
from datetime import datetime, timedelta

SECRET_KEY = "your_secret_key"

def hash_password(password):
    return generate_password_hash(password)

def verify_password(password, hashed):
    return check_password_hash(hashed, password)

def generate_token(user_id):
    payload = {
        'user_id': str(user_id),
        'exp': datetime.utcnow() + timedelta(days=1)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm='HS256')
