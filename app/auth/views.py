from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user

from .. import db
from ..models import User
from . import auth
from .forms import LoginForm, RegistrationForm


@auth.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()
    if form.validate_on_submit():

        user = User.query.filter_by(username=form.username.data).first()
        if user is not None and user.verify_password(
                form.password.data):
            login_user(user)

            return redirect(url_for('user.index'))

        else:
            flash('Invalid email or password.')

    return render_template('auth/login.html', form=form, title='Login')

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data,
                    username = form.username.data,
                    password=form.password.data)

        db.session.add(user)
        db.session.commit()
        flash('Successfully Registered')

        return redirect(url_for('auth.login'))

    return render_template('auth/signup.html', form=form, title='Register')

@auth.route('/logout')
@login_required
def logout():

    logout_user()
    flash('You have successfully been logged out.')

    return redirect(url_for('auth.login'))