from sqlalchemy.sql.expression import desc
from .db import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from sqlalchemy.dialects.postgresql import ENUM

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    __mapper_args__ = {
        'polymorphic_identity': 'user',
        'polymorphic_on': 'discriminant'
    }

    DISCRIMINANT_TYPES = [
        # key, value
        ('stood', 'Student'),
        ('ta', 'Teaching Assistant')
    ]
    # TODO OAuth with github
    id = db.Column(db.Integer, primary_key=True)
    # github username
    username = db.Column(db.String(40), nullable=False, unique=True)
    # github email
    email = db.Column(db.String(255), nullable=False, unique=True)
    hashed_password = db.Column(db.String(255), nullable=False)
    discriminant = db.Column(db.String(55), nullable=False)

    @property
    def related_role(self):
        # can be built out to be a switch case fi there are more types of user.
        return self.stood if self.discriminant('stood') else self.ta
    # ChoiceTypes, is essentially ENUM apparently there's some spiffy locale stuff you can do with this, but i don't really get locale
    # ChoiceType defaults to be a Unicode(255) column which is why in the docs you see u'stood' instead of 'stood', default is just that, so we only have to specify for ta's.
    # # the [0][0] nonsense is to keep it dynamic.

    stood = db.relationship(
        'Stood',
        uselist=False,
        backref=(db.backref('user', uselist=False)),
        lazy='joined'
        )

    ta = db.relationship(
        'TA',
        uselist=False,
        backref=(db.backref('user', uselist=False)),
        lazy='joined'
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

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "heroku_url": self.heroku_url,
            "scorecard_url": self.scorecard_url
        }


class TA(User):
    __mapper_args__ = {
        'polymorphic_identity': 'ta'
    }

    id = db.Column(
        db.Integer,
        db.ForeignKey('users.id'),
        primary_key=True
        )

    def to_dict(self):
        return super().to_dict()
