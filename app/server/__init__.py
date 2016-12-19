from flask import Blueprint

main = Blueprint('server', __name__)

from . import views
