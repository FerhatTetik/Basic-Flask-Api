from flask import request, jsonify, render_template, redirect, url_for
from app.models.models import db, Admin

def add_admin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        is_super_admin = request.form.get('is_super_admin') == 'on'  # Checkbox değerini boolean'a çevir
        new_admin = Admin(username=username, password=password, is_super_admin=is_super_admin)
        db.session.add(new_admin)
        db.session.commit()
        return redirect(url_for('admins'))
    return render_template('admin_add.html')

def update_admin(id):
    admin = Admin.query.get(id)
    if not admin:
        return redirect(url_for('admins'))

    if request.method == 'POST':
        admin.username = request.form['username']
        admin.password = request.form['password']
        admin.is_super_admin = request.form.get('is_super_admin') == 'on'  # Checkbox değerini boolean'a çevir
        db.session.commit()
        return redirect(url_for('admins'))

    return render_template('admin_update.html', admin=admin)
    
def delete_admin(id):
    admin = Admin.query.get(id)
    if admin:
        db.session.delete(admin)
        db.session.commit()
        return jsonify({'message': f'Admin {id} deleted successfully'}), 200
    else:
        return jsonify({'message': f'Admin {id} not found'}), 404

    
def admin_list():
    admins = Admin.query.all()
    return render_template('admin_list.html', admins=admins)