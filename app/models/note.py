from .db import db


class Note(db.Model):
    __tablename__ = 'notes'

    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.ForeignKey('questions.id'))
    author_id = db.Column(db.ForeignKey('users.id'))
    body = db.Column(db.Text)

    # question = db.relationship("Question", backref="notes")
