from flask_sqlalchemy import SQLAlchemy
from app import app


db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    residence = db.Column(db.String(80), nullable=False)
    profession = db.Column(db.String(80), nullable=False)
    hobby = db.Column(db.String(80), nullable=False)
    username = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username
