from .db import db
from .attachmentbase import AttachmentBase


class ResolutionAttachment(AttachmentBase):
    __tablename__ = 'resolution_attachment'
    id = db.Column(
        db.ForeignKey('attachments.id'),
        primary_key=True)

    resolution_id = db.Column(
        db.ForeignKey('resolutions.id')
        )

    __mapper_args__ = {
        "polymorphic_identity": 'resolution_attachment',
    }
