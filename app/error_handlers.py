# app/error_handlers.py

from flask import flash, redirect, url_for
from flask_jwt_extended import JWTManager

def register_error_handlers(app):
    jwt = JWTManager(app)

    @jwt.unauthorized_loader
    def unauthorized_loader_callback(callback):
        flash("Lütfen önce giriş yapınız.")
        return redirect(url_for('login_view'))

    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        flash("Oturum süreniz doldu, lütfen tekrar giriş yapınız.")
        return redirect(url_for('login_view'))

    @jwt.invalid_token_loader
    def invalid_token_callback(callback):
        flash("Geçersiz token, lütfen tekrar giriş yapınız.")
        return redirect(url_for('login_view'))

    @jwt.revoked_token_loader
    def revoked_token_callback(jwt_header, jwt_payload):
        flash("Bu token iptal edildi, lütfen tekrar giriş yapınız.")
        return redirect(url_for('login_view'))

    @jwt.needs_fresh_token_loader
    def needs_fresh_token_callback(jwt_header, jwt_payload):
        flash("Lütfen tokenınızı yenileyiniz.")
        return redirect(url_for('login_view'))
