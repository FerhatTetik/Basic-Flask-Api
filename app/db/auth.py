from flask import request, jsonify, render_template, redirect, url_for, make_response
from flask_jwt_extended import create_access_token, set_access_cookies, unset_jwt_cookies
from app.models.models import Admin

def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        admin = Admin.query.filter_by(username=username).first()
        if admin and admin.password == password:
            access_token = create_access_token(identity=username)
            response = make_response(redirect(url_for('anaSayfa')))
            set_access_cookies(response, access_token)
            return response
        else:
            return jsonify({'msg': 'Geçersiz kullanıcı adı veya şifre'}), 401

    return render_template('login.html')

def logout():
    response = make_response(redirect(url_for('login_view')))
    unset_jwt_cookies(response)
    return response