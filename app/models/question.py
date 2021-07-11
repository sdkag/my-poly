from .db import db


class Question(db.Model):
    __tablename__ = 'questions'

    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    goal = db.Column(db.Text)
    bug = db.Column(db.Text)
    error_message = db.Column(db.Text)  # eventually enum

    def to_dict(self):
        return {
            "id": self.id,
            "author_id": self.author_id,
            "goal": self.goal,
            "bug": self.bug,
            "error_message": self.error_message
        }

    def create(self):
        pass


class MetadataQuestion(db.Model):
    __tablename__ = 'metadata_questions'

    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'), primary_key=True)  # noqa
    time_question_opened = db.Column(db.String(10))
    time_question_answered = db.Column(db.String(10))
    time_question_closed = db.Column(db.String(10))
    # date = db.Column(db.Date)
    # categories = db.Column(db.String) enum
    question = db.relationship("Question", backref=db.backref("metadata", uselist=False), uselist=False)  # noqa


class Note(db.Model):
    __tablename__ = 'notes'

    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'))

    question = db.relationship("Question", backref="notes", uselist=False)


class Resolution(db.Model):
    __tablename__ = 'resolutions'

    question_id = db.Column(
        db.Integer,
        db.ForeignKey('questions.id'),
        primary_key=True
    )

    body = db.Column(db.Text)

    question = db.relationship(
        "Question",
        backref=db.backref("resolution", uselist=False), uselist=False
    )


class AttachmentBase(db.Model):
    __tablename__ = 'attachments'
    __mapper_args__ = {
        "polymorphic_identity": 'base',
        "polymorphic_on": 'attached_to'  # the descriminator
    }

    id = db.Column(db.Integer, primary_key=True)
    file_ext = db.Column(db.String(10))  # enum
    file_link = db.Column(db.String)

    attached_to = db.Column(db.String)


class NoteAttachment(AttachmentBase):
    __tablename__ = 'note_attachment'
    __mapper_args__ = {
        "polymorphic_identity": 'note_attachment',
    }
    id = db.Column(
        db.Integer,
        db.ForeignKey('attachments.id'),
        primary_key=True)

    note_id = db.Column(
        db.Integer,
        db.ForeignKey('notes.id'),
        )


class QuestionAttachment(AttachmentBase):
    __tablename__ = 'question_attachment'
    id = db.Column(
        db.Integer,
        db.ForeignKey('attachments.id'),
        primary_key=True)

    question_id = db.Column(
        db.Integer,
        db.ForeignKey('questions.id'),
    )
    __mapper_args__ = {
        "polymorphic_identity": 'question_attachment',
    }


class ResolutionAttachment(AttachmentBase):
    __tablename__ = 'resolution_attachment'
    id = db.Column(
        db.Integer,
        db.ForeignKey('attachments.id'),
        primary_key=True)

    resolution_id = db.Column(
        db.Integer,
        db.ForeignKey('resolutions.question_id')
        )

    __mapper_args__ = {
        "polymorphic_identity": 'resolution_attachment',
    }
