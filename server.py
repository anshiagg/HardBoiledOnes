from flask_bootstrap import Bootstrap
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'secret!'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////mnt/d/OneDrive/GITHUB/Python/py_flask/finish/database.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///D:\\OneDrive\\GITHUB\\Python\\hackathon\\\HardBoiledOnes\\database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


def test():
    course_dictionary = {}

    def build_class(is_lecture, start_time, hours, day):
        if is_lecture:
            return Lecture(start_time, hours, day)

        else:
            return Tutorial(start_time, hours, day)
    
    with open("MockData.txt", 'r') as file:
        spamreader = csv.reader(file, delimiter='|')
        title=True
        for row in spamreader:
            if title:
                title = False
                continue

            course_code = row[6]
            activity = row[1]

            new_class = build_class(activity == "Lecture", row[4], row[5], row[3])

            if course_code not in course_dictionary:
                course_dictionary[course_code] = Course(course_code, None, [])

        
            if activity == "Lecture":
                course_dictionary[course_code].Lecture = new_class

            else:
                course_dictionary[course_code].tutorials.append(new_class)
