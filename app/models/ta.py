from .db import db
from .user import User


class TA(User):
    __tablename__ = 'tas'
    __mapper_args__ = {
        'polymorphic_identity': 'ta'
    }

    ta_id = db.Column(
        db.ForeignKey('users.id'),
        primary_key=True,
        nullable=False
    )

    # no to_dict method, because all ta_id should be the same
    # as the user.id so all info should be in user.id
    # right now, no point in having TA model...