from flask import Flask, request, redirect, url_for
from flask_login import LoginManager, current_user
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate  # Importa Flask-Migrate
from dotenv import load_dotenv
import os
import click

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
    
    """Restrict the entire application"""
    # @app.before_request
    # def require_login():
    #     # Si el usuario no está autenticado y no está accediendo a la página de inicio de sesión
    #     if not current_user.is_authenticated and request.endpoint not in ['main.login']:
    #         return redirect(url_for('main.login'))  # Redirige a la página de inicio de sesión
        
    @app.cli.command("create_user")
    @click.argument("nombre")
    @click.argument("contraseña")
    @click.argument("gmail")
    @click.argument("rol")
    def create_user(nombre, contraseña, gmail, rol):
        """Create a new user with USERNAME, PASSWORD, GMAIL and ROL."""
        new_user = Usuario(nombre=nombre, gmail=gmail, rol=rol)
        new_user.set_password(contraseña)
        db.session.add(new_user)
        db.session.commit()
        click.echo(f"User {nombre} created successfully!")

    return app
