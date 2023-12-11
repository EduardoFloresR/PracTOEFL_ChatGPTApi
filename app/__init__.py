from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Configuración de la base de datos SQLite
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///datos.db'
    app.config['SECRET_KEY'] = 'tu_clave_secreta'

    # Inicialización de la base de datos
    db.init_app(app)

    with app.app_context():
        # Importación de modelos y creación de tablas en la base de datos
        from . import models
        db.create_all()

    # Registro de las rutas del blueprint
    from .routes import main
    app.register_blueprint(main)

    return app