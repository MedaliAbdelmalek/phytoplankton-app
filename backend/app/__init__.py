from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flasgger import Swagger
from .config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    CORS(app, origins="*", supports_credentials=True)

    Swagger(app)

    with app.app_context():
        from .routes import user_bp, main_bp  # ⬅️ importer les deux
        app.register_blueprint(user_bp, url_prefix="/auth")
        app.register_blueprint(main_bp)  # ⬅️ route de base "/"
        db.create_all()
        print("✅ Tables created!")

    return app
