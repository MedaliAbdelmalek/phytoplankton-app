from marshmallow import Schema, fields, validate

class UserSignupSchema(Schema):
    nom = fields.String(required=True)
    email = fields.Email(required=True)
    mot_de_passe = fields.String(required=True, validate=validate.Length(min=6))

class UserSigninSchema(Schema):
    email = fields.Email(required=True)
    mot_de_passe = fields.String(required=True)

class UserResponseSchema(Schema):
    id = fields.String()
    nom = fields.String()
    email = fields.Email()
    role = fields.String()
