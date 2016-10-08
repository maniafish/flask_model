from . import main
from flask import render_template
from datetime import datetime


@main.route('/', methods=['GET', 'POST'])
def home_page():
    return render_template('index.html',
                           current_time=datetime.utcnow())


@main.route('/user/<name>', methods=['GET', 'POST'])
def user_page(name):
    return render_template('user.html', name=name)
