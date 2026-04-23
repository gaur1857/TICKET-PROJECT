from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(200))
    role = db.Column(db.String(20))  # admin, agent, user

class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(500))
    status = db.Column(db.String(20), default="Open")
    priority = db.Column(db.String(20))
    created_by = db.Column(db.Integer)
    assigned_to = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
