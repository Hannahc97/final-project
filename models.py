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







class UserQuizzes(db.Model):
    __tablename__ = 'user_quizzes'
    quiz_id = db.Column(db.Integer, nullable=False,primary_key=True)
    quiz = db.Column(db.String(64), nullable=False)
    user_id = db.Column(db.String(64), db.ForeignKey('users.user_id'), nullable=False)

    def getQuiz(self):
        return self.quiz