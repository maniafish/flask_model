from . import main
from flask import render_template, redirect, url_for, session, flash
from datetime import datetime
from .forms import NameForm


@main.route('/', methods=['GET', 'POST'])
def home_page():
    return render_template('home.html',
                           current_time=datetime.utcnow())


@main.route('/user/<name>', methods=['GET', 'POST'])
def user_page(name):
    return render_template('user.html', name=name)


@main.route('/index', methods=['GET', 'POST'])
def index_page():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name and old_name != form.name.data:
            flash('Your name changed!')
        session['name'] = form.name.data
        return redirect(url_for('.index_page'))
    return render_template('index.html', form=form, name=session.get('name'))
