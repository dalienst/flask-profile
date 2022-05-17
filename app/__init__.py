from flask import Flask
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config.from_object('config.DevConfig')
app.config["JWT_SECRET_KEY"] = "5OcTNYZhbllSrR75OcTNYZhbllSrR75OcTNYZhbllSrR7"
jwt = JWTManager(app)

from app.models import db

db.create_all()

from app import routes

