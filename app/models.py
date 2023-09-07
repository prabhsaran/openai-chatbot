from .config.db import db


class Result(db.Model):
    """Model to store response details"""

    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.String(20))
    messagetype = db.Column(db.String(100))
    message = db.Column(db.String(500))
