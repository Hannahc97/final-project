from flask import Flask
from flask import render_template, redirect, url_for, flash
from forms import LoginForm, RegistrationForm
from flask_sqlalchemy import SQLAlchemy
import os
from models import *  
import sys
import uuid


uri = 'postgres://u6ra4mnc747cdk:p3b20e55cd87aab70dce4ae71024e1cea7feb1255d4b803a5737e514f68b12d5d@c9tiftt16dc3eo.cluster-czz5s0kz4scl.eu-west-1.rds.amazonaws.com:5432/dfe0sk8mnmgjpp'

if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)

app = Flask(__name__)
app.config['SECRET_KEY'] =  b'WR#&f&+%78er0we=%799eww+#7^90-;s'

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = uri
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route("/")
@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Login for {form.email.data}', 'succes')
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

if __name__ == '__main__':
    app.run(debug=True)

# DATABASE_URL = sys.argv["DATABASE_URL"]

