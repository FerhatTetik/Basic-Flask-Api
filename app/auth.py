from functools import wraps
from flask import request, jsonify, render_template, redirect, url_for, make_response
from flask_jwt_extended import create_access_token, get_jwt, set_access_cookies, unset_jwt_cookies
from app.models.models import Admin

def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = Admin.query.filter_by(username=username).first()
        if user and user.password == password:
            additional_claims = {"is_super_admin": user.is_super_admin}
            access_token = create_access_token(identity={'username': user.username}, additional_claims=additional_claims)
            response = redirect(url_for('anaSayfa'))
            set_access_cookies(response, access_token)
            return response
        else:
            return render_template('login.html', error="Invalid credentials")
    return render_template('login.html')

def logout():
    response = make_response(redirect(url_for('login_view')))
    unset_jwt_cookies(response)
    return response

def super_admin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        claims = get_jwt()
        if claims.get("is_super_admin"):
            return fn(*args, **kwargs)
        else:
            return jsonify({"msg": "Access forbidden: Super admin required"}), 403
    return wrapper
