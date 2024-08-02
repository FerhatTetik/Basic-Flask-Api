from flask import Flask, redirect, render_template, request, jsonify, url_for, make_response
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, unset_jwt_cookies, set_access_cookies
from app.config import Config
from app.models.models import Admin, db
from app.db.auth import login, logout
from app.db.users import (
    handle_users_list,
    handle_add_user,
    handle_update_user,
    handle_delete_user,
)
from app.db.books import(
    handle_add_book,
    handle_update_book,
    handle_delete_book,
    handle_books_list
)

app = Flask(__name__, template_folder='app/templates')
app.config.from_object(Config)

# JWTManager'ı başlat
jwt = JWTManager(app)

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
@jwt_required()
def anaSayfa():
    return render_template('home_page.html')

@app.route('/users')
@jwt_required()
def users_list():
    return handle_users_list()

@app.route('/users/add', methods=['GET', 'POST'])
@jwt_required()
def add_user():
    return handle_add_user()

@app.route('/users/update/<int:id>', methods=['GET', 'POST'])
@jwt_required()
def modify_user(id):
    return handle_update_user(id)

@app.route('/users/delete/<int:id>', methods=['DELETE'])
@jwt_required()
def remove_user(id):
    return handle_delete_user(id)

@app.route('/books')
@jwt_required()
def books_list():
    return handle_books_list()

@app.route('/books/add', methods=['GET', 'POST'])
@jwt_required()
def add_book():
    return handle_add_book()

@app.route('/books/update/<int:id>', methods=['GET', 'POST'])
@jwt_required()
def modify_book(id):
    return handle_update_book(id)

@app.route('/books/delete/<int:id>', methods=['DELETE'])
@jwt_required()
def remove_book(id):
    return handle_delete_book(id)

@app.route('/login', methods=['GET', 'POST'])
def login_view():
    return login()

@app.route('/logout')
def logout_view():
    return logout()

if __name__ == '__main__':
    app.run(debug=True)