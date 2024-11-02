from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate  # Importa Flask-Migrate
from dotenv import load_dotenv
import os

load_dotenv()

db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate()  # Instancia de Flask-Migrate

def create_app():
    app = Flask(__name__)

    """Configuracion"""
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['DEBUG'] = True
    
    """Inicializacion"""
    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)  # Inicializa Flask-Migrate con la app y db

    """Blueprints"""
    from app.routes.main import main
    from app.routes.incription import teams_bp
    from app.routes.sports import sport_bp
    app.register_blueprint(main)
    app.register_blueprint(teams_bp)
    app.register_blueprint(sport_bp)
    
    """Get user in each request for more info"""
    from app.models import Usuario
    login_manager.login_view = "main.login"
    login_manager.login_message_category = "danger"
    @login_manager.user_loader
    def load_user(user_id):
        return Usuario.query.get(int(user_id))

    return app
