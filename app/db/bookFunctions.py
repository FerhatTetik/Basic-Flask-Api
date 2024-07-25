from flask import request, jsonify
from app.models.models import db, Book

def create_book():
    name = request.form.get('name')
    author = request.form.get('author')
    book = Book(name=name, author=author)
    db.session.add(book)
    db.session.commit()
    return jsonify({'message': f'book {name} created with author {author}'}), 201

def get_books():
    books = Book.query.all()
    books_list = [{'id': book.id, 'name': book.name, 'author': book.author} for book in books]  # 'bookname' yerine 'name'
    return jsonify(books_list), 200

def update_book(id):
    book = Book.query.get(id)
    if book:
        book.name = request.form.get('name', book.name)
        book.author = request.form.get('author', book.author)
        db.session.commit()
        return jsonify({'message': f'book {id} updated successfully'}), 200
    else:
        return jsonify({'message': f'book {id} not found'}), 404

def delete_book(id):
    book = Book.query.get(id)
    if book:
        db.session.delete(book)
        db.session.commit()
        return jsonify({'message': f'book {id} deleted successfully'}), 200
    else:
        return jsonify({'message': f'book {id} not found'}), 404