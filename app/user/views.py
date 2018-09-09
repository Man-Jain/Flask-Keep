from flask import abort, render_template
from flask_login import current_user, login_required
from .. import db
from ..models import User, Notes

from . import user

@user.route('/')
@user.route('/index')
@login_required
def index():
	notes = Notes.query.all()
	return render_template('/user/index.html', notes = notes)

@user.route('forms')
def forms():
	return(render_template('/user/forms.html'))