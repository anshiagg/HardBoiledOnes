from flask import render_template, request, redirect, url_for, Flask
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, RadioField
from wtforms.validators import InputRequired, Email, Length
from werkzeug.security import generate_password_hash, check_password_hash
from server import *
from flask_login import login_user, login_required, logout_user, current_user
from datetime import datetime, timedelta

class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('remember me')

class RegisterForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])

@app.route('/')
def index():
    return render_template('front_page.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/search')
def search():
    course = Timetable.query.all()
    if request.method == "POST":
        course_id_list = request.form.getlist("course_id")
        for id in course_id_list:
            new_search = Search(course_id=int(id), requester_id=int(current_user.id),status=0)
            db.session.add(new_search)
            db.session.commit()
        # course = Timetable.query.filter_by(course_name=)
        return render_template('search.html', timetable=course)
    else:
        return render_template('search.html',timetable = course)

@app.route('/post')
def post():
    return render_template('post.html')

@app.route('/inbox')
def inbox():
    return render_template('inbox.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                return redirect(url_for('dashboard'))
            else:
                return render_template("login.html", form=form, login_failed=True)
        else:
            return render_template('login.html', form=form, registered=False)
    return render_template('login.html', form=form)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("login"))
    return render_template('signup.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('front_page'))

@app.route("/404")
@app.errorhandler(404)
def page_not_found(e=None):
    return render_template("base.html", content="404")