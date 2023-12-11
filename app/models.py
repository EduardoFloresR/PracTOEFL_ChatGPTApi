from . import db

class Resultado(db.Model):
    __tablename__ = 'resultados'
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.String(10))
    gradeContent = db.Column(db.Integer)
    gradeOrganization = db.Column(db.Integer)
    gradeLanguage = db.Column(db.Integer)
    gradeGrammar = db.Column(db.Integer)
    user_email = db.Column(db.String(100), db.ForeignKey('profiles.email'))
    user = db.relationship('Profile', foreign_keys=[user_email])

class Profile(db.Model):
    __tablename__ = 'profiles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    lastname = db.Column(db.String(100))
    email = db.Column(db.String(100))
    password = db.Column(db.String(100))
    salt = db.Column(db.String(100))