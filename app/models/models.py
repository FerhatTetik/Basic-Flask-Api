from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Numeric

db = SQLAlchemy()

user_book = db.Table('user_book',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('book_id', db.Integer, db.ForeignKey('book.id'), primary_key=True),
    db.Column('quantity', db.Integer, nullable=False)
)

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
<<<<<<< HEAD
    books = db.relationship('Book', secondary=user_book, backref=db.backref('users', lazy=True))
=======
    book_quantity = db.Column(db.Integer, nullable=True)    
>>>>>>> 14f69c740acbcd664c4ea4e50d219b53481d04b4

class Book(db.Model):
    __tablename__ = 'book'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    author = db.Column(db.String(120), nullable=False)
<<<<<<< HEAD
    price = db.Column(Numeric(precision=10, scale=2), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
=======
    price = db.Column(db.Integer, nullable=False)
    stock = db.Column(db.Integer, nullable=False)
>>>>>>> 14f69c740acbcd664c4ea4e50d219b53481d04b4
