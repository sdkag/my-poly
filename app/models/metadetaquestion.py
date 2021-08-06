from .db import db


class MetadataQuestion(db.Model):
    __tablename__ = 'metadata_questions'

    question_id = db.Column(db.ForeignKey('questions.id'), primary_key=True)  # noqa
    time_question_opened = db.Column(db.Time, server_default=db.func.now())
    time_question_answered = db.Column(db.Time)
    time_question_closed = db.Column(db.Time)
    # date = db.Column(db.Date)
    # categories = db.Column(db.String) enum
    question = db.relationship("Question", backref=db.backref("metadata", uselist=False))  # noqa
