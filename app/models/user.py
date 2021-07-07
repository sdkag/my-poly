from .db import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    __mapper_args__ = {
        'polymorphic_identity': 'user',
        'polymorphic_on': 'discriminant'
    }
    #TODO OAuth with github
    id = db.Column(db.Integer, primary_key = True)
    #github username
    username = db.Column(db.String(40), nullable = False, unique = True)
    #github email
    email = db.Column(db.String(255), nullable = False, unique = True)
    hashed_password = db.Column(db.String(255), nullable = False)

    discriminant = db.Column(db.String(10), nullable)
    @property
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email
        }


class Stood(User):
    __mapper_args__ = {
        'polymorphic_identity': 'stood'
    }

    id = db.Column(
        db.Integer,
        db.ForeignKey('users.id'),
        primary_key=True
        )

    heroku_url = db.Column(db.String)
    scorecard_url = db.Column(db.String)



class TA(User):
    __mapper_args__ = {
        'polymorphic_identity': 'ta'
    }

    id = db.Column(
        db.Integer,
        db.ForeignKey('users.id'),
        primary_key=True
        )