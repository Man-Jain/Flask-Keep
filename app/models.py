from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), index=True, unique=True)
    username = db.Column(db.String(60), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    notes = db.relationship('Notes', backref='user', lazy='dynamic')
    """
    Defines the one to many relationship of notes and users.
    1. Notes is taken as one user can have many notes. 
    2. backref creates a new attribute in the notes model from where we can
       use note.user to get note's owner.
    3. lazy is set dynamic as data will be in large number and hence could
       be loaded dynamically.
    """

    @property
    def password(self):
        """
        Prevent pasword from being accessed
        """
        raise AttributeError('password is not a readable attribute.')

    @password.setter
    def password(self, password):
        """
        Set password to a hashed password
        """
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """
        Check if hashed password matches actual password
        """
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User: {}>'.format(self.username)


# Set up user_loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Notes(db.Model):
    __tablename__ = 'notes'

    note_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(9999))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    # Notes will have a id of user as its foreign key.

    def __repr__():
        return '<Note: {}>'.format(self.title)