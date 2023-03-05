from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField 
from wtforms.validators import DataRequired, Email, Length


class RegisterForm(FlaskForm):
    Name = StringField(label='Name', validators=[DataRequired(), Length(min=3, max=30)])
    Email_Address = StringField(label='Email Address', validators=[DataRequired(), Email(), Length(min=3, max=30)])
    password = StringField( label='password', validators=[DataRequired(), Length(min=3, max=30)])
    
    
class LoginForm(FlaskForm):
    Name = StringField(label='Name', validators=[DataRequired(), Length(min=3, max=30)])
    Email_Address = StringField(label='Email Address', validators=[DataRequired(), Email(), Length(min=3, max=30)])
    Keep_me_signed_in = BooleanField(label='Keep_me_signed_in')