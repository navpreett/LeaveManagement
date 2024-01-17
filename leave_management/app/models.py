# app/models.py
from app import db

class LeaveRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    reason = db.Column(db.String(255), nullable=False)
    date = db.Column(db.Date, nullable=False)
