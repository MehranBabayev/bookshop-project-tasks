from extensions import db, login_manager
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import app


@login_manager.user_loader
def load_user(user_id):
    return Userman.query.get(user_id)


class Userman(UserMixin, db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    name = db.Column(db.String(40), nullable = False)
    username = db.Column(db.String(40), unique = True, nullable = False)
    email = db.Column(db.String(50), nullable = False)
    password = db.Column(db.String(255), nullable = False)
    def __repr__(self) :
        return self.name
    
    def __init__(self, name, username, email, password):
        self.name = name
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    def save(self):
        db.session.add(self)
        db.session.commit()