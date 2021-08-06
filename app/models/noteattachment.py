from .db import db
from .attachmentbase import AttachmentBase


class NoteAttachment(AttachmentBase):
    __tablename__ = 'note_attachment'
    __mapper_args__ = {
        "polymorphic_identity": 'note_attachment',
    }
    id = db.Column(
        db.ForeignKey('attachments.id'),
        primary_key=True)

    note_id = db.Column(
        db.ForeignKey('notes.id'),
        )
