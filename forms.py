from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, BooleanField, TextAreaField, SelectField, FieldList, FormField
from wtforms.validators import DataRequired, EqualTo, Email, ValidationError

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirmpassword = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password', message="Passwords must match")])
    submit = SubmitField('Register')


class QuestionForm(FlaskForm):
    text = StringField('Question', validators=[DataRequired()])
    correct = StringField('Correct Answer', validators=[DataRequired()])
    wrong1 = StringField('Wrong Answer 1', validators=[DataRequired()])
    wrong2 = StringField('Wrong Answer 2', validators=[DataRequired()])
    wrong3 = StringField('Wrong Answer 3', validators=[DataRequired()])

class QuizForm(FlaskForm):
    quizTitle = StringField('Quiz Title', validators=[DataRequired()])
    quizDescription = TextAreaField('Quiz Description', validators=[DataRequired()])
    difficulty = SelectField('Difficulty Level', choices=[(1, '1'), (2, '2'), (3, '3')], coerce=int)
    questions = FieldList(FormField(QuestionForm), min_entries=1, max_entries=10)
    submit = SubmitField('Create Quiz')





