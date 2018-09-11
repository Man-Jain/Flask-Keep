from flask_restful import Api, Resource
from . import api, rest
from .. import db
from ..models import Notes, User

class Note(Resource):
	"""docstring for Note"""
	def get(self):
		dicti = {}
		notes = Notes.query.all()
		return {'notes':notes.title}

rest.add_resource(Note, '/notes')
