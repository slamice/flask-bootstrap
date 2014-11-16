from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length

class LoginForm(Form):
    openid = StringField('openid', validators = [DataRequired()])
    remember_me = BooleanField('remeber_me', default=False) 

class EditForm(Form):
    about_me = TextAreaField('about_me', validators=[Length(min=0,max=400)])
    first_name = StringField('first_name', validators=[Length(min=0,max=50)])
    last_name = StringField('last_name', validators=[Length(min=0,max=50)])