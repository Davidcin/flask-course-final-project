from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    
    password = PasswordField('Password',validators = [DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('Register')
    def username_validation(self, username):
        username_exist = User.query.filter_by(username=username.data)
        if username_exitst:
            raise ValidationError("The username already exists! Change it !")


class LoginForm(FlaskForm):
    username_login = StringField('Email', validators=[DataRequired(),])
    password = PasswordField('Password', validators=[DataRequired(),])
    submit = SubmitField("Log In")


class AddPhone(FlaskForm):
    name = StringField('Size', validators=[DataRequired(),])