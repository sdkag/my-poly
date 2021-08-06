from .db import db


class Question(db.Model):
    __tablename__ = 'questions'

    id = db.Column(db.Integer, primary_key=True)
    # author_id = db.Column(db.ForeignKey('stoods.id'))
    author_id = db.Column(db.ForeignKey('users.id'))
    goal = db.Column(db.Text)
    bug = db.Column(db.Text)
    error_message = db.Column(db.Text)  # eventually enum, when we get an errors table
    # this way in the route we can add auth so only the op can mark question as answered.
    resolved_status = db.Column(db.Enum('open', 'archived', 'closed', 'retired',name='status', ))
    #1
    # retired = db.Column(db.Boolean, default=False)  # user doesn't want the answer anymore (or too much time has gone by)

    @property
    def resolution(self):
        return self.resolution

    # we're just going to put the answer directly on the model
    @resolution.setter
    def resolution(self, resolution):
        self.resolution = resolution

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







# all_the_joins = db.Table(
#     'attachment_entity',
#     db.Column(db.ForeignKey('attachments'))
# )
