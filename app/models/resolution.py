from .db import db


class Resolution(db.Model):
    __tablename__ = 'resolutions'
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.ForeignKey('questions.id'))
    author_id = db.Column(db.ForeignKey('users.id'))
    body = db.Column(db.Text)
    # author_id = db.Column(db.ForeignKey('tas.id'))
    # a question can only have one resolution.
    question = db.relationship(
        "Question",
        backref=db.backref("resolution", uselist=False)
    )
