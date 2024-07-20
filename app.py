from flask import Flask
from flask import render_template, redirect, url_for, flash
from forms import LoginForm
import sys

app = Flask(__name__)
app.config['SECRET_KEY'] =  b'WR#&f&+%78er0we=%799eww+#7^90-;s'

@app.route("/")
@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Login for {form.username.data}', 'succes')
        return redirect(url_for('index.html'))
    return render_template('login.html', title='Sign in', form=form)

# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     form = RegistrationForm()
#     if form.validate_on_submit():
#         flash(f'Registration for {form.username.data} received', 'success')
#         return redirect(url_for('index'))
#     return render_template('registration.html', title='Register', form=form)

if __name__ == '__main__':
    app.run(debug=True)

# DATABASE_URL = sys.argv["DATABASE_URL"]

