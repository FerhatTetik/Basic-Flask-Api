from flask import Flask, redirect, render_template, request, jsonify, url_for, make_response
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, unset_jwt_cookies, set_access_cookies
from app.config import Config
from app.models.models import Admin, db, User
from app.db.crudFonksiyonları import (
    handle_users_list,
    handle_add_user,
    handle_update_user,
    handle_delete_user,
    handle_books_list,
    handle_add_book,
    handle_update_book,
    handle_delete_book
)

app = Flask(__name__, template_folder='app/templates')
app.config.from_object(Config)

# JWT ayarları
app.config['JWT_TOKEN_LOCATION'] = ['cookies']
app.config['JWT_COOKIE_CSRF_PROTECT'] = False

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
def users_list():
    return handle_users_list()

@app.route('/users/add', methods=['GET', 'POST'])
def add_user():
    return handle_add_user()

@app.route('/users/update/<int:id>', methods=['GET', 'POST'])
def modify_user(id):
    return handle_update_user(id)

@app.route('/users/delete/<int:id>', methods=['DELETE'])
@jwt_required()
def remove_user(id):
    return handle_delete_user(id)

@app.route('/books')
def books_list():
    return handle_books_list()

@app.route('/books/add', methods=['GET', 'POST'])
def add_book():
    return handle_add_book()

@app.route('/books/update/<int:id>', methods=['GET', 'POST'])
def modify_book(id):
    return handle_update_book(id)

@app.route('/books/delete/<int:id>', methods=['DELETE'])
@jwt_required()
def remove_book(id):
    return handle_delete_book(id)

# Giriş rotası
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        admin = Admin.query.filter_by(username=username).first()
        if admin and admin.password == password:  # In production, use hashed passwords
            access_token = create_access_token(identity=username)
            response = make_response(redirect(url_for('anaSayfa')))
            set_access_cookies(response, access_token)
            return response
        else:
            return jsonify({'msg': 'Geçersiz kullanıcı adı veya şifre'}), 401

    return render_template('login.html')

# Çıkış rotası
@app.route('/logout')
def logout():
    response = make_response(redirect(url_for('login')))
    unset_jwt_cookies(response)
    return response

if __name__ == '__main__':
    app.run(debug=True)
