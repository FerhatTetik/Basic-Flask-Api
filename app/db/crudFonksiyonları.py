from flask import request, jsonify, render_template, redirect, url_for
from app.models.models import db, User, Book, user_book

from flask import request, jsonify, render_template, redirect, url_for
from app.models.models import db, User, Book, user_book

def create_user(): #request model oluşturulursa kod iyileştirmesi daha iyi olur.
    name = request.form.get('name')
    email = request.form.get('email')
<<<<<<< HEAD
    book_ids = request.form.getlist('book_ids[]')
    quantities = request.form.getlist('quantities[]')

    if not name or not email or not book_ids or not quantities:
        return jsonify({'message': 'Name, email, books and quantities are required'}), 400

    user = User(name=name, email=email)
=======
    quantity = request.form.get('quantity')
    if not name or not email:
        return jsonify({'message': 'Name and email are required'}), 400
    user = User(name=name, email=email, quantity=quantity)
>>>>>>> 14f69c740acbcd664c4ea4e50d219b53481d04b4
    db.session.add(user)
    db.session.commit()

    total_price = 0
    for book_id, quantity in zip(book_ids, quantities):
        book = Book.query.get(book_id)
        if book:
            book_quantity = int(quantity)
            if book.quantity < book_quantity:
                return jsonify({'message': f'Not enough stock for book {book.name}'}), 400
            db.session.execute(user_book.insert().values(user_id=user.id, book_id=book.id, quantity=book_quantity))
            total_price += book.price * book_quantity
            book.quantity -= book_quantity

    db.session.commit()

    return jsonify({'message': f'User {name} created with email {email} and total price {total_price}'}), 201

def get_users():
    users = User.query.all()
    return users

def update_user(id):
    user = User.query.get(id)
    if user:
        user.name = request.form.get('name', user.name)
        user.email = request.form.get('email', user.email)
        user.quantity = request.form.get('quantity', user.quantity)
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
<<<<<<< HEAD
    quantity = request.form.get('quantity')
    if not name or not author:
        return jsonify({'message': 'Name and author are required'}), 400
    book = Book(name=name, author=author, price=price,quantity=quantity)
=======
    stock = request.form.get('stock')
    if not name or not author:
        return jsonify({'message': 'Name and author are required'}), 400
    book = Book(name=name, author=author, price=price, stock=stock)
>>>>>>> 14f69c740acbcd664c4ea4e50d219b53481d04b4
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
<<<<<<< HEAD
        book.quantity = request.form.get('quantity', book.quantity)
=======
        book.stock = request.form.get('stock', book.stock)
>>>>>>> 14f69c740acbcd664c4ea4e50d219b53481d04b4
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
    users = User.query.all()
    user_data = []
    
    for user in users:
        user_books = db.session.query(user_book).filter_by(user_id=user.id).all()
        total_price = 0
        books = []
        
        for user_book_entry in user_books:
            book = Book.query.get(user_book_entry.book_id)
            quantity = user_book_entry.quantity
            total_price += book.price * quantity
            books.append({'name': book.name, 'quantity': quantity})
        
        user_data.append({'user': user, 'books': books, 'total_price': total_price})
    
    return render_template('users_list.html', user_data=user_data)


def handle_add_user():
    if request.method == 'POST':
        response, status_code = create_user()
        if status_code == 201:
            return redirect(url_for('users_list'))
        else:
            return response, status_code

    books = get_books()
    return render_template('add_user.html', books=books)

def handle_update_user(id):
    user = User.query.get(id)
    if not user:
        return jsonify({'message': f'User {id} not found'}), 404

    if request.method == 'POST':
        user.name = request.form.get('name', user.name)
        user.email = request.form.get('email', user.email)
        
        book_ids = request.form.getlist('book_ids[]')
        quantities = request.form.getlist('quantities[]')
        
        if not book_ids or not quantities:
            return jsonify({'message': 'Kitap ve adedi girin.'}), 400
        
        db.session.execute(user_book.delete().where(user_book.c.user_id == user.id))

        for book_id, quantity in zip(book_ids, quantities):
            book = Book.query.get(book_id)
            if book:
                book_quantity = int(quantity)
                if book.quantity < book_quantity:
                    return jsonify({'message': f'Not enough stock for book {book.name}'}), 400
                db.session.execute(user_book.insert().values(user_id=user.id, book_id=book.id, quantity=book_quantity))
                book.quantity -= book_quantity
        
        db.session.commit()
        return redirect(url_for('users_list'))

    books = Book.query.all()
    return render_template('update_user.html', user=user, books=books)


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
