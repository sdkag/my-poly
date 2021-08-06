from .db import db
from .attachmentbase import AttachmentBase


class QuestionAttachment(AttachmentBase):
    __tablename__ = 'question_attachment'
    id = db.Column(
        db.ForeignKey('attachments.id'),
        primary_key=True)

    # constraint on this so. it can only be picked from the answers whos question_id is this one. (i.e. the ones that show up in question.resolutions)
    question_id = db.Column(
        db.ForeignKey('questions.id'),
    )
    __mapper_args__ = {
        "polymorphic_identity": 'question_attachment',
    }
