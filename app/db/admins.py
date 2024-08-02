from flask import request, jsonify, render_template, redirect, url_for
from app.models.models import db, Admin

def add_admin():
    username= request.form.get('username')
    password= request.form.get('password')
    if not username or not password:
        return jsonify({'message': 'username and password are required'}), 400
    admin = Admin(username=username, password=password)
    db.session.add(admin)
    db.session.commit()
    return jsonify({'message': f'Admin User {username} created'}), 201

def update_admin(id):
    admin = Admin.query.get(id)
    if admin:
        admin.username = request.form.get('name', admin.name)
        admin.password = request.form.get('password', admin.password)
        db.session.commit()
        return jsonify({'message': f'admin {id} updated successfully'}), 200
    else:
        return jsonify({'message': f'admin {id} not found'}), 404
    
def delete_admin(id):
    admin = Admin.query.get(id)
    if admin:
        db.session.delete(admin)
        db.session.commit()
        return jsonify({'message': f'admin {id} deleted successfully'}), 200
    else:
        return jsonify({'message':f'admin {id} not found'})