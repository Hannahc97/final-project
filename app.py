from datetime import datetime, timedelta
from flask import Flask
from flask import render_template, redirect, url_for, flash, request, jsonify, make_response
from forms import LoginForm, RegistrationForm
from flask_sqlalchemy import SQLAlchemy
import os
import database
import sys
import uuid
from flask_login import current_user, login_user, logout_user, login_required
from urllib.parse import urlsplit
from extensions import login
from data import quizzes
from logic import quiz as quizbuilder

QUIZZES = quizzes.QUIZZES

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
        resp = make_response(redirect(url_for('dashboard')))
        resp.set_cookie('uuid', user.get_id(), expires=datetime.now() + timedelta(days=365*10))
        return resp 
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
            resp = make_response(redirect(url_for('home')))
            resp.set_cookie('uuid', user_id, expires=datetime.now() + timedelta(days=365*10))
            return resp 
        except Exception as e: 
            print(e)
    return render_template('sign_up.html', title='Register', form=form)

@app.route('/logout')
def logout():
    logout_user()
    resp = make_response(redirect(url_for('home')))
    resp.set_cookie('uuid', '', expires=0)
    return resp

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/quiz')
@login_required
def quiz():
    uuid_cookie = request.cookies.get('uuid')
    user = userRegister.query.filter_by(user_id=uuid_cookie).first()
    quiz_info = ""
    for quiz in QUIZZES:
        quizTitle = quiz["title"]
        quizDescription = quiz["description"]
        quiz_id = quiz["quiz_id"]
        adaptive_url = f"http://127.0.0.1:5000/quiz-page?quiz_id={quiz_id}&difficulty_level=" + str(user.difficulty_level_status())
        non_adaptive_url = f"http://127.0.0.1:5000/quiz-page?quiz_id={quiz_id}"
        quiz_info += f"Title: {quizTitle}<br> Description: {quizDescription}<br>Adaptive Quiz: {adaptive_url}<br>Non Adaptive Quiz: {non_adaptive_url}<br><br>"

    return render_template('quiz.html',QUIZZES=quiz_info)

@app.route('/quiz-page')
@login_required
def quizpage():
    quiz_id = request.args.get("quiz_id")
    difficulty_level = request.args.get("difficulty_level")
    if not difficulty_level:
        quiz = quizbuilder(int(quiz_id)).generateNonAdaptive()
    else:
        quiz = quizbuilder(int(quiz_id),int(difficulty_level)).generateAdaptive()
    return jsonify(quiz)
    

    return render_template('quiz.html',QUIZZES=quiz_info)






if __name__ == '__main__':
    app.run(debug=True)

# DATABASE_URL = sys.argv["DATABASE_URL"]