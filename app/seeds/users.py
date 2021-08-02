from werkzeug.security import generate_password_hash
from app.models import db, Stood, TA


# Adds a demo user, you can add other users here if you want
def seed_users():
    demo_stood = Stood()
    demo_stood.username = 'Demo'
    demo_stood.email = 'demo@aa.io'
    demo_stood.password = 'password'

    db.session.add(demo_stood)
    demo_ta = TA()
    demo_ta.username = 'sdkag'
    demo_ta.email = 'sa@aa.io'
    demo_ta.password = 'password'
    db.session.add(demo_ta)
    db.session.commit()


def undo_users():
    db.session.execute('TRUNCATE users RESTART IDENTITY CASCADE;')
    db.session.commit()
