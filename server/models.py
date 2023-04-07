from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'

    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.Integer)

    @validates('name')
    def validate_name(self, key, name):
        names = db.session.query(Author.name).all()
        if not name:
            raise ValueError("requires each record to have a name")
        elif name in names:
            raise ValueError("Name must be unique")
        return name 
    
    
    @validates('phone_number')
    def validate_phone_number(self, key, number):
        if len(number) !=10:
            raise ValueError("Invalid phone number")
        return number
    
class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable = False)
    content = db.Column(db.String)
    summary = db.Column(db.String)
    category = db.Column(db.String)

    @validates('summary', 'content')
    def validate_length(self, key, string):
        if (key == 'content'):
            if len(string) <= 250:
                raise ValueError("Must be greater than 250")
        if (key == 'summary'):
            if len(string) >= 250:
                raise ValueError("Must be less than 250")
        return string
    
    @validates('category')
    def validate_category(self, key, category):
        if category != 'Fiction' and category != 'Non-Fiction':
            raise ValueError("must be Fuction or non-fiction")
        return category 