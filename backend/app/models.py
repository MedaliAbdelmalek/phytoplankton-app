from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID
import uuid
from datetime import datetime
from enum import Enum as PyEnum
from . import db

class RoleEnum(PyEnum):
    ADMIN = "ADMIN"
    EXPERT = "EXPERT"
    UTILISATEUR = "UTILISATEUR"

class TypeModeleEnum(PyEnum):
    YOLO = "YOLO"
    RESNET = "RESNET"

class Utilisateur(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nom = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    mot_de_passe = db.Column(db.String(200), nullable=False)
    role = db.Column(db.Enum(RoleEnum), default=RoleEnum.UTILISATEUR)
    date_creation = db.Column(db.DateTime, default=datetime.utcnow)

    projets = db.relationship('Projet', backref='utilisateur', lazy=True)
    validations = db.relationship('Validation', backref='utilisateur', lazy=True)

class Projet(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nom = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=True)
    date_debut = db.Column(db.DateTime)
    date_fin = db.Column(db.DateTime)
    utilisateur_id = db.Column(UUID(as_uuid=True), db.ForeignKey('utilisateur.id'), nullable=False)

    images = db.relationship('Image', backref='projet', lazy=True)

class ModeleIA(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nom = db.Column(db.String(100), nullable=False)
    type = db.Column(db.Enum(TypeModeleEnum))
    date_creation = db.Column(db.DateTime, default=datetime.utcnow)
    chemin_modele = db.Column(db.String(255), nullable=False)

    images = db.relationship('Image', backref='modele_ia', lazy=True)
    especes_crees = db.relationship('Espece', backref='modele_createur', lazy=True)
    validations = db.relationship('Validation', backref='modele_ia', lazy=True)

class Espece(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nom_scientifique = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=True)
    image_reference = db.Column(db.String(255), nullable=True)
    cree_par_modele_id = db.Column(UUID(as_uuid=True), db.ForeignKey('modele_ia.id'))

    images = db.relationship('Image', backref='espece', lazy=True)

class Image(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    chemin_fichier = db.Column(db.String(255), nullable=False)
    taille = db.Column(db.Float)
    fluorescence = db.Column(db.Float)
    position = db.Column(db.String(100))
    date_capture = db.Column(db.DateTime)

    projet_id = db.Column(UUID(as_uuid=True), db.ForeignKey('projet.id'))
    modele_ia_id = db.Column(UUID(as_uuid=True), db.ForeignKey('modele_ia.id'))
    espece_id = db.Column(UUID(as_uuid=True), db.ForeignKey('espece.id'))

    validation = db.relationship('Validation', backref='image', lazy=True, cascade='all, delete-orphan')
    annotee = db.relationship('ImageAnnote', backref='image', uselist=False)
    non_annotee = db.relationship('ImageNonAnnote', backref='image', uselist=False)

class ImageAnnote(db.Model):
    image_id = db.Column(UUID(as_uuid=True), db.ForeignKey('image.id'), primary_key=True)
    score_confiance = db.Column(db.Float, nullable=False)
    annotee_par = db.Column(UUID(as_uuid=True), db.ForeignKey('utilisateur.id'))

class ImageNonAnnote(db.Model):
    image_id = db.Column(UUID(as_uuid=True), db.ForeignKey('image.id'), primary_key=True)
    en_attente_depuis = db.Column(db.DateTime, default=datetime.utcnow)

class Validation(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    utilisateur_id = db.Column(UUID(as_uuid=True), db.ForeignKey('utilisateur.id'))
    image_id = db.Column(UUID(as_uuid=True), db.ForeignKey('image.id'))
    modele_ia_id = db.Column(UUID(as_uuid=True), db.ForeignKey('modele_ia.id'))
    date_validation = db.Column(db.DateTime, default=datetime.utcnow)
    commentaire = db.Column(db.Text)
