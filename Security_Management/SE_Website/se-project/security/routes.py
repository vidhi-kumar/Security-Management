from flask import Flask
from security import app, db, bcrypt
from security.forms import RegistrationForm, LoginForm
from security.models import User, Post
# dont forget to add Post to line 4
from flask import render_template, url_for, flash, redirect
from flask_login import login_user, current_user, logout_user



# posts = [
#     {
#         'type' : 'WatchMan',
#         'units' : 10,
#         'date' : '10/10/19'
#     },
#     {
#         'type' : 'BodyGuard',
#         'units' : 2,
#         'date' : '16/12/19'
#     }
# ]
posts=User.query.all()
@app.route('/')
def index():
    posts = User.query.all()
    return render_template('home.html', posts=posts)
@app.route('/home')
def home():
    index()
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/register', methods=['GET', 'POST'])
def register():
    # if current_user.is_authenticated:
        # return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash('form.password.data').decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to login', 'success')
        return redirect(url_for('login'))
        # return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    # if current_user.is_authenticated:
        # return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        # hashed_password = bcrypt.generate_password_hash('form.password.data').decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Your Security is now our Responsibility !', 'success')
        return redirect(url_for('home'))
        # return redirect(url_for('home'))
    return render_template('dashboard.html', title='Dashboard', form=form)

# @app.route('/data')
# def data():
#     return render_template('data.html', posts=posts)

@app.route("/login", methods=['GET', 'POST'])
def login():
    # if current_user.is_authenticated:
    #     return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data.lower()).first()
        if user:
            login_user(user, remember=form.remember.data)
            # next_page = request.args.get('next')
            return redirect(url_for('dashboard'))
        else:
            flash('Unsuccessful Login! Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)
# @app.route("/login", methods=['GET', 'POST'])
# def login():
#     # if current_user.is_authenticated:
#         # return redirect(url_for('home'))
#     form = LoginForm()
#     if form.validate_on_submit():
#         user = User.query.filter_by(email=form.email.data).first()
#         if user and bcrypt.check_password_hash(user.password, form.password.data):
#         # if user:
#             # if(user.password==form.password.data):
#             login_user(user, remember=form.remember.data)
#                 # next_page = request.args.get('next')
#             return redirect(url_for('home'))
#         # else:
#         #         flash('Login Unsuccessful. Please check email and password', 'danger')
#         else:
#             flash('Login Unsuccessful. Please check email and password', 'danger')
#     return render_template('login.html', title='Login', form=form)


# @app.route("/account")
# def account():
#     return render_template('account.html', title='Account')


# @app.route("/logout")
# def logout():
#     logout_user()
    # return redirect(url_for('home'))
