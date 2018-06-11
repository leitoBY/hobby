from connection import db
from flask import Blueprint

database_api = Blueprint('database_api', __name__)


@database_api.route('/create_all')
def create_all_tables():
    db.create_all()
    return "data tables were successfully created!"
