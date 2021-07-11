from flask import Blueprint, jsonify
from flask_login import login_required
from app.models import User

user_routes = Blueprint('users', __name__)


@user_routes.route('/')
@login_required
def users():
    users = User.query.all()

    [stoods, tas] = [[], []]
    for u in users:
        if u.discriminant == 'stood':
            stoods.append(u)
        else:
            tas.append(u)

    return {
        "users": [user.to_dict() for user in users],
        "stoods": [s.to_dict() for s in stoods],
        "tas": [t.to_dict() for t in tas]
        }


@user_routes.route('/<int:id>')
@login_required
def user(id):
    user = User.query.get(id)
    return user.to_dict()

@user_routes.route('/me')
@login_required
def current_user():
    current_user
    return user.to_dict()
