from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from werkzeug.utils import secure_filename
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)

app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

class LoginForm(FlaskForm):
    username = StringField('id астронавта', validators=[DataRequired()])
    password = PasswordField('Пароль астронавта', validators=[DataRequired()])
    id_captain = StringField('id капитана', validators=[DataRequired()])
    password_captain = PasswordField('Пароль капитана', validators=[DataRequired()])
    '''photo = FileField(validators=[FileRequired()])'''
    submit = SubmitField('Доступ')
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    '''
    if form.validate_on_submit():
        return redirect('/success')
        '''
    return render_template('login.html', title='Аварийный доступ', form=form)

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')