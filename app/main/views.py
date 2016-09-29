from . import main
from flask import render_template


@main.route('/', methods=['GET', 'POST'])
def home_page():
    return render_template('index.html')


@main.route('/user/<name>', methods=['GET', 'POST'])
def user_page(name):
    return render_template('user.html', name=name)
