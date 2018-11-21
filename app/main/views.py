"""
Blueprint main
"""

from flask import render_template
from . import main
from ..models import User
from flask_login import login_user, logout_user, login_required, current_user
from .forms import GenerateKeyFrom


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/user/<username>', methods=['GET', 'POST'])
@login_required
def user(username):
    form = GenerateKeyFrom()
    if form.validate_on_submit():
        hasp_id = form.hasp_id.data
        musk = form.musk.data
        password = form.password.data
        clays = form.clays.data
        data = hasp_id + musk + password + clays
        data = data.encode('utf8')
        return render_template('user.html', user=user, form=form, data=data)
    return render_template('user.html', user=user, form=form)
