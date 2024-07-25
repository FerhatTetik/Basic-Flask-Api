from flask import Flask, render_template, request
from app.config import Config
from app.models.models import db, User
from app.db.crudFonksiyonları import create_user, get_users, delete_user, update_user

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/users')
def users_list():
    users = get_users()  # get_users() fonksiyonunu kullan
    return render_template('users_list.html', users=users)

@app.route('/users/add', methods=['GET', 'POST'])
def add_user():
    create_user()
    return render_template('add_user.html')

@app.route('/users/update/<int:id>', methods=['PUT'])
def modify_user(id):
    return update_user(id)

@app.route('/users/delete/<int:id>', methods=['DELETE'])
def remove_user(id):
    return delete_user(id)

@app.route('/')
def anaSayfa():
    return render_template('home_page.html')

if __name__ == '__main__':
    app.run(debug=True)
