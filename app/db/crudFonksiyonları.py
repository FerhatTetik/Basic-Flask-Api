from flask import request, jsonify
from app.models.user_model import db, User

def create_user():
    name = request.form.get('name')
    email = request.form.get('email')
    user = User(name=name, email=email)
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': f'User {name} created with email {email}'}), 201

def get_users():
    users = User.query.all()
    users_list = [{'id': user.id, 'name': user.name, 'email': user.email} for user in users]  # 'username' yerine 'name'
    return jsonify(users_list), 200

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