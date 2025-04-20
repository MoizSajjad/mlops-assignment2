#intializes the flask ap, sets up DB, JWTT, and register routes
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS

db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    CORS(app)

    # Configs
    app.config.from_object("app.config.Config")

    # Init extensions
    db.init_app(app)
    jwt.init_app(app)

    # Register blueprints
    from app.auth.routes import auth_bp
    app.register_blueprint(auth_bp, url_prefix="/api/auth")

    with app.app_context():
        db.create_all()

    return app
