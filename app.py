from flask import Flask
from app.config import Config
from app.models.user_model import db, User
from app.db.crudFonksiyonları import create_user, get_users, delete_user, update_user

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/users/add', methods=['POST'])
def add_user():
    return create_user()

@app.route('/users', methods=['GET'])
def get_all_users():
    return get_users()

@app.route('/users/update/<int:id>', methods=['PUT'])
def modify_user(id):
    return update_user(id)

@app.route('/users/delete/<int:id>', methods=['DELETE'])
def remove_user(id):
    return delete_user(id)

@app.route('/')
def anaSayfa():
    return 'Ana Sayfa'

if __name__ == '__main__':
    app.run(debug=True)
