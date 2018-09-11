from flask import abort, render_template, flash, redirect, url_for
from flask_login import current_user, login_required

from .. import db
from ..models import Notes
from .forms import NotesForm
from . import user

@user.route('/')
@user.route('/index')
@login_required
def index():
	notes = Notes.query.all()
	return render_template('/user/index.html', notes = notes)

@user.route('/forms', methods = ['GET', 'POST'])
@login_required
def forms():
	form = NotesForm()
	if form.validate_on_submit():
		note = Notes(title=form.title.data,
					 description=form.description.data,
					 user_id=current_user.id)
		db.session.add(note)
		db.session.commit()
		flash('Note Saved')
		return redirect(url_for('user.forms'))

	return(render_template('/user/forms.html', form=form, title='Add Note'))