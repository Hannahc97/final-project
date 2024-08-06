import json
import database
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from extensions import login 

db = database.DB


# user_id: A unique identifier for each user, 
# # email: The user's email address, which must be unique.
# password_hash: The hashed password for secure authentication.
class userRegister(UserMixin, db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.String(64), primary_key=True, nullable=False, unique=True, index=True)
    email = db.Column(db.String(64), nullable=False, unique=True, index=True)
    password_hash = db.Column(db.String(64), nullable=False)
    difficulty_level = db.Column(db.String(64), nullable=False)

    def hashPassword(self):
        self.password_hash = generate_password_hash(self.password_hash)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_id(self):
        return str(self.user_id)
    
    def difficulty_level_status(self,quiz_id):
        return json.loads(str(self.difficulty_level).replace("'",'"'))[str(quiz_id)]["difficulty"]
    
    def set_difficulty_level_status(self,quiz_id,difficulty):
        all_difficulties = json.loads(str(self.difficulty_level).replace("'",'"'))
        all_difficulties[str(quiz_id)].update({"difficulty":int(difficulty)})
        self.difficulty_level = json.dumps(all_difficulties)
        return True
    
@login.user_loader
def load_user(user_id):
    return userRegister.query.get(user_id)




# Represents a quiz which contains multiple questions.
# Defines a quiz's title and description, and relates to the questions it contains
# quiz_id: A unique identifier for each quiz, 
# # title: The title of the quiz, 
# # description: A short description of the quiz
# questions: A relationship to the Question model, indicating that a quiz can have multiple questions
# class Quiz(db.Model):
#     __tablename__ = 'quizzes'
#     quiz_id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
#     title = db.Column(db.String(128), nullable=False)
#     description = db.Column(db.String(256))
#     questions = db.relationship('Question', backref='quiz', lazy=True)

# Represents individual questions in a quiz.
# Contains the text of the question and relates to the possible answers.
# question_id: A unique identifier for each question, 
# quiz_id: A foreign key linking the question to a specific quiz
# text: The text of the question
# difficulty level from 1 (easy) to 5 (hard)
# answers: A relationship to the Answer model, indicating that a question can have multiple answers
# class Question(db.Model):
#     __tablename__ = 'questions'
#     question_id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
#     quiz_id = db.Column(db.Integer, db.ForeignKey('quizzes.quiz_id'), nullable=False)
#     text = db.Column(db.String(256), nullable=False)
#     difficulty = db.Column(db.Integer, nullable=False)  
#     answers = db.relationship('Answer', backref='question', lazy=True)

# Represents possible answers for a question.
# Contains the text of the answer and a boolean indicating if it's the correct answer
# answer_id: A unique identifier for each answer
# question_id: A foreign key linking the answer to a specific question
# text: The text of the answer
# is_correct: A boolean indicating if this answer is correct
class quizResults(db.Model):
    __tablename__ = 'quizresults'
    user_id = db.Column(db.String(64),primary_key=True, nullable=False, unique=True, index=True)
    results = db.Column(db.String(256), nullable=False)
    quiz_title = db.Column(db.String(256), nullable=False)
    quiz_id = db.Column(db.Integer, nullable=False)
    difficulty_level = db.Column(db.Integer, nullable=False)

# Tracks which quizzes a user has taken and their scores.
# Records the relationship between a user and a quiz, including the score and completion time
# user_quiz_id: A unique identifier for each user-quiz relationship
# user_id: A foreign key linking to a specific user
# quiz_id: A foreign key linking to a specific quiz
# score: The score the user achieved on the quiz
# completed_at: The date and time when the user completed the quiz
# class UserQuiz(db.Model):
#     __tablename__ = 'user_quizzes'
#     user_quiz_id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
#     quiz_id = db.Column(db.Integer, db.ForeignKey('quizzes.quiz_id'), nullable=False)
#     score = db.Column(db.Integer)
#     completed_at = db.Column(db.DateTime)

# Tracks the answers provided by users for each question in a quiz.
# Records the selected answers for each question by a user during a quiz attempt.
# user_answer_id: A unique identifier for each user answer
# user_quiz_id: A foreign key linking to a specific user-quiz relationship
# question_id: A foreign key linking to a specific question
# answer_id: A foreign key linking to a specific answer
# answered_at: The date and time when the user answered the question
# class UserAnswer(db.Model):
#     __tablename__ = 'user_answers'
#     user_answer_id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
#     user_quiz_id = db.Column(db.Integer, db.ForeignKey('user_quizzes.user_quiz_id'), nullable=False)
#     question_id = db.Column(db.Integer, db.ForeignKey('questions.question_id'), nullable=False)
#     answer_id = db.Column(db.Integer, db.ForeignKey('answers.answer_id'), nullable=False)
#     answered_at = db.Column(db.DateTime)

# Track the performance of a user on different difficulty levels
# user_performance_id: A unique identifier for each performance record.
# user_id: A foreign key linking to the user.
# quiz_id: A foreign key linking to the quiz.
# difficulty_level: The difficulty level being tracked.
# correct_answers: The number of correct answers given by the user at this difficulty level.
# total_answers: The total number of answers given by the user at this difficulty level.
class UserPerformance(db.Model):
    __tablename__ = 'user_performance'
    user_performance_id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quizzes.quiz_id'), nullable=False)
    difficulty_level = db.Column(db.Integer, nullable=False)
    correct_answers = db.Column(db.Integer, nullable=False, default=0)
    total_answers = db.Column(db.Integer, nullable=False, default=0)
