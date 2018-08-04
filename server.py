from flask_bootstrap import Bootstrap
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'secret!'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////mnt/d/OneDrive/GITHUB/Python/py_flask/finish/database.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///D:\\OneDrive\\GITHUB\\Python\\hackathon\\\HardBoiledOnes-login\\database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


class Post(db.Model):
    __tablename__ = 'post'

    id = db.Column(db.Integer, primary_key=True)
    poster_id = db.Column(db.Integer)
    course_id = db.Column(db.Integer)

# or request
class Search(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer)
    requester_id = db.Column(db.Integer)
    status = db.Column(db.Integer)

class Timetable(db.Model):
    __tablename__ = 'timetable'

    id = db.Column(db.Integer,primary_key=True)
    type = db.Column(db.String())
    day = db.Column(db.String())
    start_time = db.Column(db.Integer)
    duration = db.Column(db.Integer)
    course_name = db.Column(db.String())
    def __repr__(self):
        return "<Course name='%s', type='%s', day='%s', time='%s', duration='%s'>"(self.course_name, self.type, self.day, self.time, self.duration)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
