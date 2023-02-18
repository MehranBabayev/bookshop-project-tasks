from extensions import db
from datetime import datetime

from app import app

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key =True)
    Your_Name = db.Column(db.String(100))
    Email_Address = db.Column(db.String(100))
    Message = db.Column(db.String(255))
    
    
    def __init__(self, Your_Name, Email_Address, Message):
        self.Your_Name = Your_Name
        self.Email_Address = Email_Address
        self.Message = Message
        
    def __repr__(self):
        return self.Your_Name
    
    def save(self):
        db.session.add(self)
        db.session.commit()
        
        



class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100),unique=True, nullable=False)
    author = db.Column(db.String(40),unique=True, nullable=False)
    price = db.Column(db.Float,default=10.00 )
    description = db.Column(db.Text,nullable=True)
    image_url = db.Column(db.String(255),unique=True, nullable=False)
    stock = db.Column(db.Boolean,default=True)
    genre = db.Column(db.String(40), nullable=False)
    language = db.Column(db.String(40), nullable=False)
    publisher = db.Column(db.String(40), nullable=False)
    
    
    def __repr__ (self):
        return self.title
    
    def __init__ (self,title, author,description, image_url, stock, genre, language, publisher):
        self.title = title
        self.author = author
        self.description = description
        self.image_url = image_url
        self.stock = stock
        self.genre = genre
        self.language = language
        self.publisher = publisher
        
        
    def save(self):
        db.session.add(self)
        db.session.commit()        