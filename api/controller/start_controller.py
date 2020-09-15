from flask import Blueprint


start = Blueprint('start', __name__)

@start.route('/')
def index():
    return 'Welcome Educanutri API', 200