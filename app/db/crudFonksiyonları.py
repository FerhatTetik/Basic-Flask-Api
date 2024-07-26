from flask import request, jsonify, render_template, redirect, url_for
from app.models.models import db, User

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
