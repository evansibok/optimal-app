"""
Database Models
"""
from datetime import datetime
from optimal import db


class User(db.Model):
    """
    Creates a database table for Users
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return f"<User {self.username}>"

class Post(db.Model):
    """
    Creates a database table for Posts
    """
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    title = db.Column(db.String(140))
    content = db.Column(db.String)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return f"<Title {self.title}, Content {self.content}>"
