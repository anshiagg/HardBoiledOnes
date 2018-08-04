from flask import Flask 
from flask_login import LoginManager


app = Flask(__name__)
app.secret_key = 'this_is_a_secret_key'