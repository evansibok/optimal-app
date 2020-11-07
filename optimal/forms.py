from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=15, message='Username should be between 2 and 15 characters')])

    email = StringField('Email Address', validators=[DataRequired(), Email(message='Enter a valid email address!')])

    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, message='Password should be at least 8 characters!')])

    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password', message="Passwords don't match")])

    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email Address', validators=[DataRequired(), Email(message='Enter a valid email address!')])

    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, message='Password should be at least 8 characters!')])

    remember_me = BooleanField('Remember Me')

    submit = SubmitField('Login')
