from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,PasswordField,validators
from wtforms.widgets import PasswordInput
import email_validator
from wtforms.validators import DataRequired


app = Flask(__name__)
app.config['SECRET_KEY'] = 'C2HWGVoMGfNTBsrYQg8EcMrdTimkZfAb'

class EmailForm(FlaskForm):
    email = StringField('Email',[DataRequired(),validators.Length(min=6, max=120), validators.Email()])
    password = PasswordField('Password',[DataRequired(),validators.Length(min=6, max=120)])
    submit = SubmitField('Log IN')

@app.route("/")
def home():
    return render_template('index.html',)
@app.route("/login",methods= ['Get','POST'])
def login():
    form = EmailForm()
    if form.validate_on_submit():
        if (form.email.data == 'admin@email.com' and form.password.data == '12345678'):
            return render_template('success.html')
        else:
            return render_template("denied.html")
    return render_template('login.html',form =form)

if __name__ == '__main__':
    app.run(debug=True)