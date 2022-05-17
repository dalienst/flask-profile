from flask import request,abort
from app import app
from app.models import User
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from app.models import db

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import unset_jwt_cookies
from flask import jsonify


@app.route("/register", methods=["POST"])
def register():
    data = request.json
    fname = data.get("fname")
    email = data.get("email")
    residence = data.get("residence")
    profession = data.get("profession")
    hobby = data.get("hobby")
    username = data.get("username")
    password = data.get("password")

    errors = {}

    if not fname:
        errors["fname"] = "First name is required!"
    if not email:
        errors["email"] = "Email is required!"
    if not residence:
        errors["residence"] = "Residence is required!"
    if not profession:
        errors["profession"] = "Profession is required!"
    if not hobby:
        errors["hobby"] = "Hobby is required!"
    if not username:
        errors["username"] = "Username is required!"
    if not password:
        errors["password"] = "Password is required!"

    if len(errors.keys()) != 0:
        abort(400, {"errors": errors})

    user = User(fname=fname, email=email, residence=residence, profession=profession, hobby=hobby, username=username,password=generate_password_hash(password))
    db.session.add(user)
    db.session.commit()
    return {"message": "User created"}, 201

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    user = User.query.filter_by(username = username).first()

    if user:
        response = check_password_hash(user.password, password)
        if response:
            access_token = create_access_token(identity= {"Name":user.fname, "Username": user.username, "Email":user.email, "Residence":user.residence, "Profession":user.profession, "Hobby":user.hobby})
            return jsonify(access_token=access_token), 200
        else:
            return {"message": "Invalid credentials"}, 400

@app.route("/index", methods=["GET"])
@jwt_required()
def home():
    identity = get_jwt_identity()
    return identity

# @app.route("/profile", methods=["POST"])
# @jwt_required()
# def profile():
#     data = request.json
#     residence = data.get("residence")
#     profession = data.get("profession")


@app.route("/update/<id>", methods=["PUT"])
@jwt_required()
def update(id):
    data = request.json
    user = User.query.filter_by(id=id).first()
    if user:
        user.fname = data.get("fname")
        user.email = data.get("email")
        user.residence = data.get("residence")
        user.profession = data.get("profession")
        user.hobby = data.get("hobby")
        user.username = data.get("username")
        db.session.commit()
        return {"message":"User updated"}, 200
    return {"message":"User not found"}, 404



@app.route("/logout", methods=["POST", "GET"])
@jwt_required()
def logout():
    response = jsonify({"message":"Logged Out"})
    unset_jwt_cookies(response)  
    return response, 200

