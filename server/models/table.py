from server import db
from server.models._base import MyBase


class Table(MyBase):
    __tablename__ = "table"

    id = db.Column(db.Text, primary_key=True)
    number = db.Column(db.Text, nullable=False)

    courses = db.relationship("Course", backref='table')
