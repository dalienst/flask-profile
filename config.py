import os

file_path = os.path.abspath(os.getcwd())+"/db/profile.db"

class Config:
    SECRET_KEY="xSwkoPwfszoe821St8ewwZi76eEQVC9n"
    DEVELOPMENT=False
    DEBUG=False
    TESTING=False
    SQLALCHEMY_DATABASE_URI=""
    SQLALCHEMY_TRACK_MODIFICATIONS=True


class DevConfig(Config):
    DEVELOPMENT=True
    DEBUG=True
    SQLALCHEMY_DATABASE_URI=f"sqlite:///{file_path}"