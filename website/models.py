from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

#ALL notes have to comply with the following requirements 
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now()) #Get the current date
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) #user foreign key to reference the user object 
    #foreign key is used only when we have one-to-many relationship
    
#ALL my users have to comply with the following requirements 
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True) #no user can have same email together
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')
    

    