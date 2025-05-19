from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # Charger la config depuis le fichier
    app.config.from_object(Config)
    
    db.init_app(app)

    with app.app_context():
        from .routes import main  # importer le blueprint
        app.register_blueprint(main)  # enregistrer le blueprint
        db.create_all()
        print("✅ tables created !!")


    return app
