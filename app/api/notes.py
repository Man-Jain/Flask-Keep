from flask_restful import Api, Resource
from . import api, rest
from .. import db
from ..models import Notes, User

class Note(Resource):
	"""docstring for Note"""
	def get(self):
		dicti = {}
		notes = Notes.query.all()
		for a in notes:
			dicti[a] = [a.note_id, a.title, a.description]

		return dicti

rest.add_resource(Note, '/notes')
