from sqlalchemy.sql.expression import desc
from .db import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
# from sqlalchemy.dialects.postgresql import ENUM


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    __mapper_args__ = {
        'polymorphic_identity': 'users',
        'polymorphic_on': 'discriminant'
    }

    # TODO OAuth with github, update username and email to match github creds
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    hashed_password = db.deferred(db.Column(db.String(255), nullable=False))

    discriminant = db.Column(
        db.Enum("stood", "ta", name="role"),
        nullable=False
    )


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
