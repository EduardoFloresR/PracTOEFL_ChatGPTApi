# Importación del objeto de la base de datos (db) desde el módulo actual
from . import db

# Definición de la clase Resultado que hereda de db.Model (modelo de SQLAlchemy)
class Resultado(db.Model):
    # Nombre de la tabla en la base de datos
    __tablename__ = 'resultados'
    
    # Definición de columnas en la tabla 'resultados'
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.String(10))
    gradeContent = db.Column(db.Integer)
    gradeOrganization = db.Column(db.Integer)
    gradeLanguage = db.Column(db.Integer)
    gradeGrammar = db.Column(db.Integer)
    
    # Clave foránea que referencia la columna 'email' en la tabla 'profiles'
    user_email = db.Column(db.String(100), db.ForeignKey('profiles.email'))
    
    # Relación con la clase Profile, utilizando la clave foránea user_email
    user = db.relationship('Profile', foreign_keys=[user_email])

# Definición de la clase Profile que hereda de db.Model (modelo de SQLAlchemy)
class Profile(db.Model):
    # Nombre de la tabla en la base de datos
    __tablename__ = 'profiles'
    
    # Definición de columnas en la tabla 'profiles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    lastname = db.Column(db.String(100))
    email = db.Column(db.String(100))
    password = db.Column(db.String(100))
    salt = db.Column(db.String(100))
