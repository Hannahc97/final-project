from flask import Flask
from flask import render_template, redirect, url_for, flash, request
from forms import LoginForm, RegistrationForm
from flask_sqlalchemy import SQLAlchemy
import os
import database
import sys
import uuid
from flask_login import current_user, login_user, logout_user, login_required
from urllib.parse import urlsplit
from extensions import login

app = Flask(__name__)

db = database.buildDb().build(app)

from models import userRegister, Quiz, Question, Answer, UserQuiz, UserAnswer, UserPerformance

app.config['SECRET_KEY'] =  b'WR#&f&+%78er0we=%799eww+#7^90-;s'

basedir = os.path.abspath(os.path.dirname(__file__))


login.init_app(app)
login.login_view = 'login'





@app.route("/")
@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    # if current_user.is_authenticated:
    #     return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = userRegister.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid email or password', 'danger')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        flash(f'Login for {form.email.data}', 'success')
        return redirect(url_for('home'))
    return render_template('login.html', title='Sign in', form=form)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegistrationForm()
    if form.validate_on_submit():
        user_id = str(uuid.uuid4())
        new_user = userRegister(email=form.email.data, password_hash=form.password.data, user_id=user_id)
        new_user.hashPassword()
        db.session.add(new_user)
        try:
            db.session.commit()
            flash(f'Registration for {form.email.data} received', 'success')
            return redirect(url_for('home'))
        except Exception as e: 
            print(e)
    return render_template('sign_up.html', title='Register', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/quiz')
@login_required
def quiz():
    return render_template('quiz.html')


if __name__ == '__main__':
    app.run(debug=True)

# DATABASE_URL = sys.argv["DATABASE_URL"]