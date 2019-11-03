from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
# from flask import render_template, url_for, flash, redirect
# from forms import Registration, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '59471c063c01'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # added for error redemption
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

from security import routes