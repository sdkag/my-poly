```py
from sqlalchemy_utils import ChoiceType

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    __mapper_args__ = {
        'polymorphic_identity': 'user',
        'polymorphic_on': 'discriminant'
    }

    # DISCRIMINANT_TYPES = [
    #     # key, value
    #     ('stood', 'Student'),
    #     ('ta', 'Teaching Assistant')
    # ]
    # TODO OAuth with github
    id = db.Column(db.Integer, primary_key=True)
    # github username
    username = db.Column(db.String(40), nullable=False, unique=True)
    # github email
    email = db.Column(db.String(255), nullable=False, unique=True)
    hashed_password = db.Column(db.String(255), nullable=False)
    # ChoiceTypes, is essentially ENUM apparently there's some spiffy locale stuff you can do with this, but i don't really get locale
    # ChoiceType defaults to be a Unicode(255) column which is why in the docs you see u'stood' instead of 'stood', default is just that, so we only have to specify for ta's.
    # # the [0][0] nonsense is to keep it dynamic.
    # discriminant = db.Column(ChoiceType(DISCRIMINANT_TYPES, impl=db.String()),default=DISCRIMINANT_TYPES[0][0], nullable=False)
    discriminant = db.Column(db.String(55), nullable=False)
```
