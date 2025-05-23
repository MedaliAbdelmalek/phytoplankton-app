from flask import request, jsonify
from ..services import user_service
from ..schemas.user_schema import UserSignupSchema, UserSigninSchema, UserResponseSchema
from marshmallow import ValidationError

signup_schema = UserSignupSchema()
signin_schema = UserSigninSchema()
response_schema = UserResponseSchema()

def signup():
    try:
        data = signup_schema.load(request.json)
        user = user_service.create_user(data)
        return response_schema.dump(user), 201
    except ValidationError as err:
        return {'errors': err.messages}, 400
    except ValueError as e:
        return {'error': str(e)}, 400

def signin():
    try:
        data = signin_schema.load(request.json)
        token, user = user_service.authenticate_user(data['email'], data['mot_de_passe'])
        return {
            'token': token,
            'user': response_schema.dump(user)
        }, 200
    except ValidationError as err:
        return {'errors': err.messages}, 400
    except ValueError as e:
        return {'error': str(e)}, 401

def get_users():
    users = user_service.get_all_users()
    return response_schema.dump(users, many=True), 200
