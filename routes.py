from flask import render_template, request, redirect, url_for
from datetime import datetime, timedelta
from flask_login import login_user, logout_user, current_user, login_required
from server import app

@app.route('/404')
@app.errorhandler(404)
def page_not_found(e=None):
    return render_template('404.html'), 404

@app.route('/')
def index():
	return render_template('home.html')

@app.route('/login')
def login():
	return render_template('login.html')