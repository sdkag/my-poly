from .db import db


class AttachmentBase(db.Model):
    __tablename__ = 'attachments'
    __mapper_args__ = {
        "polymorphic_identity": 'base',
        "polymorphic_on": 'attached_to'  # the descriminator
    }

    id = db.Column(db.Integer, primary_key=True)
    file_ext = db.Column(db.String(10))  # enum
    file_link = db.Column(db.String)
    # will be attached to either a question, note, or resolution.
    attached_to = db.Column(db.String)
