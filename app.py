from flask import Flask, render_template
from flask_migrate import Migrate
from app.config import Config
from app.models.models import db
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

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
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
def remove_book(id):
    return handle_delete_book(id)

if __name__ == '__main__':
    app.run(debug=True)
