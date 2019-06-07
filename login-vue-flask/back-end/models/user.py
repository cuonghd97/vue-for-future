import bcrypt

from db import db


class User(db.Document):
    username = db.StringField(max_length=200)
    password = db.StringField(max_length=200)
