from werkzeug.security import generate_password_hash
from app.models import db, User, TA, Stood
from faker import Faker
# Adds a demo user, you can add other users here if you want


def seed_users(number_of_stoods):
    # an object with lots of fake methods to generate data.
    # print(fake.__dict__()) run this line to see all the methods available to you. there are a lot
    fake = Faker()
    [username, email] = [fake.user_name, fake.email] # for code readability below
  # change this if we want more randomly genereated users

    db.session.execute('TRUNCATE users RESTART IDENTITY CASCADE;') # wipe the table first.

    demo = User(username='demo', email='demo@aa.io', password='password')

    db.session.add(demo)

    stoods = [
        Stood(username=username(), email=email(), password='password')
        for _ in range(number_of_stoods)
    ]

    tas = [
        TA(username='sagawu', email='sagawu@aa.io', password='password'),
        TA(username='jsummers', email='jsummers@aa.io', password='password'),
        TA(username='obyrnes', email='obyrnes@aa.io', password='password'),
        TA(username='rdalton', email='rdalton@aa.io', password='password'),
    ]

    db.session.add_all(stoods)
    db.session.flush()
    db.session.add_all(tas)
    db.session.commit()
    return {
        "stoods": stoods,
        "tas" : tas
        }


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and resets
# the auto incrementing primary key
def undo_users():
    db.session.execute('TRUNCATE users RESTART IDENTITY CASCADE;')
    db.session.commit()
