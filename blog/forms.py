from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo,ValidationError
from blog.models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()]) 
    password_confirmation = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField("Register")


    def validate_username(self,username):
        user = User.query.filter_by(username = username.data).first()
        if user:
            raise ValidationError('username is already taken please choose a different one!!!')

    def validate_email(self,email):
        email = User.query.filter_by(email = email.data).first()
        if email:
            raise ValidationError('email is already taken please choose a different one!!!')




class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me =  BooleanField('Remember me')
    submit = SubmitField("Login")


class ApdateAccountForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    picture = FileField('update profile picture', validators=[FileAllowed(['jpeg','jpg','png'])])
    submit = SubmitField("Update")


    def validate_username(self,username):
        if current_user.username != username.data:
            user = User.query.filter_by(username = username.data).first()
            if user:
                raise ValidationError('username is already taken please choose a different one!!!')

    def validate_email(self,email):
        if current_user.email != email.data:
            email = User.query.filter_by(email = email.data).first()
            if email:
                raise ValidationError('email is already taken please choose a different one!!!')


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')

