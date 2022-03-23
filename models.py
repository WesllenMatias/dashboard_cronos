from enum import unique
#from app import db
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin
from main import login_manager


@login_manager.user_loader
def get_user(user_id):
    return User.query.filter_by(user_id).frist()


class User(db.model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer,autoincrement=True, primary_key=True)
    name = db.Column(db.String(100),nullable=False)
    email = db.Column(db.String(100),nullable=False,unique=True)
    password = db.Column(db.String(128),nullable=False)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = generate_password_hash(password)

    def verify_password(self, pwd):
        return check_password_hash(self.password, pwd)

