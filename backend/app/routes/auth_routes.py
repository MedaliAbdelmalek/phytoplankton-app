from flask import Blueprint
from ..controllers import user_controller
from flasgger import swag_from

user_bp = Blueprint('user', __name__)

@user_bp.route('/signup', methods=['POST'])
@swag_from({
    'tags': ['Auth'],
    'description': 'Register a new user',
    'parameters': [
        {
            'in': 'body',
            'name': 'body',
            'schema': {
                '$ref': '#/definitions/UserSignupSchema'
            }
        }
    ],
    'responses': {
        201: {'description': 'User created successfully'},
        400: {'description': 'Validation error'}
    }
})
def signup():
    return user_controller.signup()

@user_bp.route('/signin', methods=['POST'])
@swag_from({
    'tags': ['Auth'],
    'description': 'Authenticate user',
    'parameters': [
        {
            'in': 'body',
            'name': 'body',
            'schema': {
                '$ref': '#/definitions/UserSigninSchema'
            }
        }
    ],
    'responses': {
        200: {'description': 'Login successful'},
        401: {'description': 'Invalid credentials'}
    }
})
def signin():
    return user_controller.signin()

@user_bp.route('/users', methods=['GET'])
def get_users():
    return user_controller.get_users()
