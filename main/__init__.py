from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '586bd7052c41f36601557dbb77a1fb93'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///saknniDB.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
from main import routs
