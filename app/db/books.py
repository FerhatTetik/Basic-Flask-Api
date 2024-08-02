from flask import request, jsonify, render_template, redirect, url_for
from app.models.models import db, Book

def create_book():
    name = request.form.get('name')
    author = request.form.get('author')
    price = request.form.get('price')
    quantity = request.form.get('quantity')
    if not name or not author:
        return jsonify({'message': 'Name and author are required'}), 400
    book = Book(name=name, author=author, price=price, quantity=quantity)
    db.session.add(book)
    db.session.commit()
    return jsonify({'message': f'Book {name} created with author {author}'}), 201

def get_books():
    books = Book.query.all()
    return books

def update_book(id):
    book = Book.query.get(id)
    if book:
        book.name = request.form.get('name', book.name)
        book.author = request.form.get('author', book.author)
        book.price = request.form.get('price', book.price)
        book.quantity = request.form.get('quantity', book.quantity)
        db.session.commit()
        return jsonify({'message': f'Book {id} updated successfully'}), 200
    else:
        return jsonify({'message': f'Book {id} not found'}), 404

def delete_book(id):
    book = Book.query.get(id)
    if book:
        db.session.delete(book)
        db.session.commit()
        return jsonify({'message': f'Book {id} deleted successfully'}), 200
    else:
        return jsonify({'message': f'Book {id} not found'}), 404

def handle_books_list():
    books = get_books()
    return render_template('books_list.html', books=books)

def handle_add_book():
    if request.method == 'POST':
        response, status_code = create_book()
        if status_code == 201:
            return redirect(url_for('books_list'))
        else:
            return response, status_code
    return render_template('add_book.html')

def handle_update_book(id):
    if request.method == 'POST':
        response, status_code = update_book(id)
        if status_code == 200:
            return redirect(url_for('books_list'))
        else:
            return response, status_code
    book = Book.query.get(id)
    if book:
        return render_template('update_book.html', book=book)
    else:
        return jsonify({'message': f'Book {id} not found'}), 404

def handle_delete_book(id):
    response, status_code = delete_book(id)
    return response, status_code
