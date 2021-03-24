from . import db
from flask import request
import sqlalchemy


class User(db.Model):
    # Uncomment the line below if you want to set your own table name
    __tablename__ = "property"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    number_of_bedrooms = db.Column(db.Integer())
    number_of_bathrooms = db.Column(db.Integer())
    location = db.Column(db.String(120))
    price = db.Column(db.Float(120))
    type1 = db.Column(db.String(120))
    description = db.Column(db.String(120))
    photo = db.Column(db.String(120))


    def __init__(self, title, number_of_bedrooms,number_of_bathrooms,location,price,type1,description,photo):
        self.title = title
        self.number_of_bedrooms = number_of_bedrooms
        self.number_of_bathrooms = number_of_bathrooms
        self.location = location
        self.price = price
        self.type1 = type1
        self.description = description
        self.photo = photo

    def __repr__(self):
        return '<User %r>' % self.username