from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Email, Length, Regexp



class ContactForm(FlaskForm):
    Your_Name = StringField(label='Your Name', validators=[DataRequired(), Length(min=3, max=30)])
    Email_Address = StringField(label='Email Address', validators=[DataRequired(), Email(), Length(min=3, max=30), Regexp('.*gmail.com$', message="Email must end with gmail")])
    Message = TextAreaField( label='Message', validators=[DataRequired()])