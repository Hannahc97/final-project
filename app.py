from flask import Flask
from flask import render_template
# from forms import LoginForm, RegistrationForm
import sys

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')



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

