from flask import Blueprint, jsonify, request
from flask_login import login_required
from app.models import Question

question_routes = Blueprint('questions', __name__)


@question_routes.route('/', methods=['GET', 'POST'])
def questions():
    if request.method == 'GET':
        return {"question": [q.to_dict() for q in Question.query.all()]}
    # elif request.method == 'POST':
    #     request.json
    #     db.add(Question)
