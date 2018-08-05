from flask import render_template, request, redirect, url_for, Flask
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, RadioField
from wtforms.validators import InputRequired, Email, Length
from werkzeug.security import generate_password_hash, check_password_hash
from server import *
from flask_login import login_user, login_required, logout_user, current_user
# from System import System
# from Post import Posts
# from Requests import Request

# sys = System()

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

@app.route('/search', methods=['GET', 'POST'])
def search():
    # get the courses name form the post list
    # course_list = []
    # for temp in sys.post_list:
    #     course_list.append(temp.getCourse)
    posts = Post.query.all()
    course_list = []
    for p in posts:
        course_list.append(Timetable.query.filter(Timetable.id == p.course_id).first())

    if request.method == "POST":
        if len(request.form["searching_field"]) != 0:
            course_name = request.form["searching_field"]
            course = Timetable.query.filter(Timetable.course_name == course_name[0:8])
            return render_template('post.html', Courses=course)
        else:
            course_id_list = request.form.getlist("course_id")
            for id in course_id_list:
                # new request
                new_search = Search(course_id=int(id), requester_id=int(current_user.id),status=0)
                db.session.add(new_search)
                db.session.commit()


            return render_template('search.html', post=course_list)
    else:
        return render_template('search.html',post = course_list)

@app.route('/post', methods=['GET', 'POST'])
def post():
    course = Timetable.query.all()
    if request.method == "POST":
        if len(request.form["searching_field"]) != 0:
            course_name = request.form["searching_field"]
            course = Timetable.query.filter(Timetable.course_name == course_name[0:8])
            return render_template('post.html', Courses=course)
        else:
            course_id_list = request.form.getlist("course_id")
            # use database to find posted courselist
            for iterator in course_id_list:
                c = Timetable.query.filter(Timetable.id == iterator).first()
                # sys.addPost(Post(current_user, c))

                # add to post table
                db.session.add(Post(poster_id=current_user.id, course_id=c.id))
                db.session.commit()

        return render_template('post.html', Courses=course)
    else:
        return render_template('post.html',Courses=course)

@app.route('/inbox', methods=['GET', 'POST'])
def inbox():
    # check the search database
    request_list = Search.query.all()
    # find any request that belongs to current user
    message_list = []
    requester = ''
    for iterator in request_list:
        # the post
        for posts in Post.query.filter(Post.course_id == iterator.course_id):
            # if this requeseted course is posted by this user
            if current_user.id == posts.poster_id:
                message_list.append(Timetable.query.filter(Timetable.id == iterator.course_id).first())
                requester = User.query.filter(User.username==iterator.requester_id).first()

    if request.method == "POST":
        message_list = []
        swap = True;
        for p in request.form.getlist("course_id"):
            message_list.append(Timetable.query.filter(Timetable.id == p).first())

        return render_template('inbox.html', Course=message_list,swap = True,requester = requester)
    else:
        return render_template('inbox.html',course=message_list)

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
    return redirect(url_for('index'))

@app.route("/404")
@app.errorhandler(404)
def page_not_found(e=None):
    return render_template("base.html", content="404")