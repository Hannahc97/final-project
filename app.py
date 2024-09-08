from datetime import datetime, timedelta
import json
from flask import Flask
from flask import render_template, redirect, url_for, flash, request, jsonify, make_response
from forms import LoginForm, RegistrationForm, QuizForm
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
import itertools
import os
import database
import sys
import uuid
from flask_login import current_user, login_user, logout_user, login_required
from urllib.parse import urlsplit
from extensions import login
from data import quizzes
from logic import quiz as quizbuilder
from logic import calculateDifficulty

QUIZZES = quizzes.QUIZZES

app = Flask(__name__)

db = database.buildDb().build(app)

from models import userRegister, quizResults, UserQuizzes

app.config['SECRET_KEY'] =  os.environ.get("SECRET_KEY")

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
        resp = make_response(redirect(url_for('quiz')))
        resp.set_cookie('uuid', user.get_id(), expires=datetime.now() + timedelta(days=365*10))
        return resp 
    return render_template('login.html', title='Sign in', form=form)



@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegistrationForm()
    if form.validate_on_submit():
        user_id = str(uuid.uuid4())
        new_user = userRegister(email=form.email.data, password_hash=form.password.data, user_id=user_id, difficulty_level=json.dumps({"1": {"difficulty": 1}, "2": {"difficulty": 1}, "3": {"difficulty": 1}, "4": {"difficulty": 1}, "5": {"difficulty": 1}, "6": {"difficulty": 1}, "7": {"difficulty": 1}, "8": {"difficulty": 1}, "9": {"difficulty": 1}}))
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

    #  checks if the request URL starts with "http", splits the URL by (:) and compares the first part with "http".
    if "http"  == request.url.split(":")[0]:
        domain = "http://127.0.0.1:5000" #If "http", assumes domain is local development server, used during development
    else: #  If not "http", then assumed to be "https".
        domain = "https://" + request.host # domain is set to the current host with "https" as the protocol.
    # retrieves a cookie named uuid, which stores a unique identifier for the user.
    uuid_cookie = request.cookies.get('uuid') 
    # queries the db to find first user whose user_id matches the uuid_cookie.
    user = userRegister.query.filter_by(user_id=uuid_cookie).first() 
    
    # Initialises an empty string that will be used to store HTML content for each quiz.
    quiz_info = "" 
    #  creates a list of all quiz IDs from the QUIZZES data, which is presumably loaded from the JSON file
    ALL_QUIZ_IDS = [quiz_id_arr["quiz_id"] for quiz_id_arr in QUIZZES]

    for quiz in QUIZZES: # Loops through each quiz in the QUIZZES list.
        if quiz.get("uuid"): #If the quiz has a uuid key, it skips this iteration of the loop.
            continue
        quizTitle = quiz["title"] # Retrieves the title of the current quiz.
        quizDescription = quiz["description"] # Retrieves the description of the current quiz.
        quiz_id = quiz["quiz_id"] # Retrieves the quiz ID of the current quiz
        try: # Attempts to execute the code within this block to determine the adaptive URL.
            current_difficulty = user.difficulty_level_status(quiz_id) # Retrieves the current difficulty level for the quiz from the user's data.
            # Constructs the URL for the adaptive quiz version using the user's current difficulty level.
            adaptive_url = f"{domain}/quiz-page?quiz_id={quiz_id}&difficulty_level=" + str(user.difficulty_level_status(quiz_id))
        except: # If there's an error this block is executed
            # If there's an exception, the adaptive URL defaults to difficulty level 1
            adaptive_url = f"{domain}/quiz-page?quiz_id={quiz_id}&difficulty_level=1"
        # Constructs URLs for non-adaptive quizzes
        non_adaptive_url = f"{domain}/quiz-page?quiz_id={quiz_id}" 

        # Appends HTML block to quiz_info that represents quiz card, including title, description, difficulty level, and links to both adaptive and non-adaptive versions of the quiz
        quiz_info += f"""
        <div class="quiz-card">
            <h2>{quizTitle}</h2>
            <p>{quizDescription}</p>
            <p class="difficulty">Adaptive Difficulty Level: {current_difficulty}</p>
            <a href='{adaptive_url}' class="quiz-link">Adaptive Quiz</a>
            <a href='{non_adaptive_url}' class="quiz-link">Non Adaptive Quiz</a>
        </div>
        """ 
    with db.engine.connect() as connection: # Opens a connection to the database
        # Executes a SQL query to get all quizzes associated with the current user from the user_quizzes table and flattens the result into a list.
        user_quizzes  = list(itertools.chain(*connection.execute(text(f"SELECT ALL quiz FROM user_quizzes WHERE user_id = '{uuid_cookie}';")).fetchall()))
    if len(user_quizzes) > 0: # Checks if there are any quizzes associated with the user.
        for each_quiz in user_quizzes: # Loops through each quiz from the database
            formatted_quiz = json.loads(each_quiz) # Parses each quiz string into a JSON object.
            quizTitle = formatted_quiz["title"] # Retrieves the title of the quiz
            quizDescription = formatted_quiz["description"]
            quiz_id = formatted_quiz["quiz_id"]
            if formatted_quiz["uuid"] != uuid_cookie: # Skips the quiz if the uuid in the quiz does not match the user's uuid
                continue
            if int(quiz_id) in ALL_QUIZ_IDS: # Skips the quiz if its ID is already in the list of all quiz IDs (to avoid duplicates).
                continue

            # Generates adaptive URL with difficulty level 1 for the user-specific quiz.   
            adaptive_url = f"{domain}/quiz-page?quiz_id={quiz_id}&difficulty_level=1"
            # Constructs URLs for non-adaptive quizzes
            non_adaptive_url = f"{domain}/quiz-page?quiz_id={quiz_id}" 

            # Appends another HTML block for the user-specific quiz to quiz_info.
            quiz_info += f"""
            <div class="quiz-card">
                <h2>{quizTitle}</h2>
                <p>{quizDescription}</p>
                <p class="difficulty">Adaptive Difficulty Level: {current_difficulty}</p>
                <a href='{adaptive_url}' class="quiz-link">Adaptive Quiz</a>
                <a href='{non_adaptive_url}' class="quiz-link">Non Adaptive Quiz</a>
            </div>
            """ 
        # Extract the unique quiz names
        # Each quiz's information is formatted into a string that includes the title, description, and links to both types of quizzes, appending it to quiz_info.
    
    # renders the quiz.html template, passing the accumulated quiz_info string as a context variable named QUIZZES. This will be used in the template to display the list of quizzes.
    return render_template('quiz.html',QUIZZES=quiz_info) 


@app.route('/quiz-page')
@login_required
def quizpage(): 
    quiz_id = request.args.get("quiz_id") # retrieves the quiz_id parameter from the URL query string, identifies which quiz the user is trying to access
    difficulty_level = request.args.get("difficulty_level") # retrieves the difficulty_level parameter from the URL query string, if provided.
    uuid_cookie = request.cookies.get('uuid') # retrieves a cookie named uuid, which stores a unique identifier for the user
    ALL_QUIZ_IDS = [quiz_id_arr["quiz_id"] for quiz_id_arr in QUIZZES] # creates a list of all quiz IDs from the QUIZZES data, which is assumed to be a list of quiz data loaded from a JSON file.

    if not int(quiz_id) in ALL_QUIZ_IDS: # Checks if the quiz_id is not in the list of all quiz IDs.
        user_quiz = UserQuizzes.query.filter_by(quiz_id=int(quiz_id)).first() # If the quiz ID is not found in ALL_QUIZ_IDS, it queries the UserQuizzes database for a quiz with the matching quiz_id.
        user_quiz = json.loads(user_quiz.getQuiz()) # Converts the quiz data retrieved from the database into a Python dictionary.
        QUIZZES.append(user_quiz) # Adds this user-specific quiz to the QUIZZES list, so it can be processed like the other quizzes
    if not difficulty_level:  # If difficulty_level is not provided, it creates an instance of the quizbuilder class with the quiz_id and calls the generateNonAdaptive method to generate a non-adaptive quiz.
        quiz = quizbuilder(int(quiz_id))
        generated_quiz = quiz.generateNonAdaptive()
        formattedQuiz = quiz.jsFormat() # Formats the quiz data into a JavaScript-compatible format, likely for embedding within the HTML.
    else: # If difficulty_level is provided, it creates an instance of the quizbuilder with quiz_id and difficulty_level, and calls the generateAdaptive method to generate an adaptive quiz.
        quiz = quizbuilder(int(quiz_id),int(difficulty_level))
        generated_quiz = quiz.generateAdaptive()
        formattedQuiz = quiz.jsFormat()    
    return render_template('quizpage.html', QUIZ_INFORMATION=formattedQuiz, QUIZ_ID=quiz_id, QUIZ_DIFFICULTY=difficulty_level,TITLE=generated_quiz["title"], DESCRIPTION=generated_quiz["description"])



@app.route('/quiz-results', methods=['POST'])
@login_required
def quizresults(): 
    data = request.get_json()
    uuid = data.get("uuid")
    quiz_id = data.get("quiz_id")
    quiz_difficulty = data.get("quiz_difficulty")
    if quiz_difficulty == "None":
        quiz_difficulty = "1"
    title = data.get("title")
    results = str(data.get("results"))
    try:
        quiz_submission = quizResults(user_id=uuid, results=results, quiz_title=title, quiz_id=quiz_id, difficulty_level=int(quiz_difficulty))
        db.session.add(quiz_submission)
        db.session.commit()
        if data.get("quiz_difficulty") != "None":
            new_difficulty = calculateDifficulty(int(quiz_difficulty), results)
            user_info = userRegister.query.filter_by(user_id=uuid).first()
            user_info.set_difficulty_level_status(quiz_id,new_difficulty)
            db.session.add(user_info)
            db.session.commit()
        

        return "Saved Successfully" ,200
    except Exception as e:
        return f"Error Saving Results: {e}", 500


@app.route('/create_quiz', methods=['GET', 'POST'])
@login_required
def create_quiz():
    form = QuizForm()
    if request.method == 'POST':
        data = request.get_json()
        uuid_cookie = request.cookies.get('uuid') 
        if not uuid_cookie:
            return "Error Authenticating", 500
        index = 1
        for question in data["questions"]:
            question["question_id"] = index
            index += 1
        data["uuid"] = uuid_cookie
        user_quizzes = UserQuizzes(quiz_id=data["quiz_id"],quiz=json.dumps(data), user_id=current_user.get_id()) 
        db.session.add(user_quizzes)
        db.session.commit()    
        return "Quiz Added", 200
    
    return render_template('create_quiz.html', form=form)



if __name__ == '__main__':
    app.run(debug=True)

# DATABASE_URL = sys.argv["DATABASE_URL"]
