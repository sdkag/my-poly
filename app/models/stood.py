from .db import db
from .user import User


class Stood(User):
    __tablename__ = 'stoods'
    __mapper_args__ = {
        'polymorphic_identity': 'stood'
    }

    stoods_id = db.Column(db.ForeignKey('users.id'), primary_key=True, nullable=False)
    heroku_url = db.Column(db.String)
    scorecard_url = db.Column(db.String)

    def to_dict(self):
        return {
            **super().to_dict,
            "id": self.id,
            "heroku_url": self.heroku_url,
            "scorecard_url": self.scorecard_url
        }