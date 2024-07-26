from flask import request, jsonify, render_template, redirect, url_for
from app.models.models import db, User, Book

def create_user():
    name = request.form.get('name')
    email = request.form.get('email')
    if not name or not email:
        return jsonify({'message': 'Name and email are required'}), 400
    user = User(name=name, email=email)
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': f'User {name} created with email {email}'}), 201

def get_users():
    users = User.query.all()
    return users

def update_user(id):
    user = User.query.get(id)
    if user:
        user.name = request.form.get('name', user.name)
        user.email = request.form.get('email', user.email)
        db.session.commit()
        return jsonify({'message': f'User {id} updated successfully'}), 200
    else:
        return jsonify({'message': f'User {id} not found'}), 404

def delete_user(id):
    user = User.query.get(id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': f'User {id} deleted successfully'}), 200
    else:
        return jsonify({'message': f'User {id} not found'}), 404
    
def create_book():
    name = request.form.get('name')
    author = request.form.get('author')
    price = request.form.get('price')
    if not name or not author:
        return jsonify({'message': 'Name and author are required'}), 400
    book = Book(name=name, author=author, price=price)
    db.session.add(book)
    db.session.commit()
    return jsonify({'message': f'book {name} created with author {author}'}), 201

def get_books():
    books = Book.query.all()
    return books

def update_book(id):
    book = Book.query.get(id)
    if book:
        book.name = request.form.get('name', book.name)
        book.author = request.form.get('author', book.author)
        book.price = request.form.get('price', book.price)
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

def handle_users_list():
    users = get_users()
    return render_template('users_list.html', users=users)

def handle_add_user():
    if request.method == 'POST':
        response, status_code = create_user()
        if status_code == 201:
            return redirect(url_for('users_list'))
        else:
            return response, status_code
    return render_template('add_user.html')

def handle_update_user(id):
    if request.method == 'POST':
        response, status_code = update_user(id)
        if status_code == 200:
            return redirect(url_for('users_list'))
        else:
            return response, status_code
    user = User.query.get(id)
    if user:
        return render_template('update_user.html', user=user)
    else:
        return jsonify({'message': f'User {id} not found'}), 404

def handle_delete_user(id):
    response, status_code = delete_user(id)
    return response, status_code

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
        return jsonify({'message': f'book {id} not found'}), 404

def handle_delete_book(id):
    response, status_code = delete_book(id)
    return response, status_code
