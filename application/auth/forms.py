from flask_wtf import FlaskForm
from wtforms import StringField
  
class LoginForm(FlaskForm):
    username = StringField("Username", render_kw={'autofocus': True})
  
    class Meta:
        csrf = False

class RegisterForm(FlaskForm):
    name = StringField("Display name", render_kw={'autofocus': True})
    username = StringField("Username")
  
    class Meta:
        csrf = False

class EditForm(FlaskForm):
    name = StringField("Display name", render_kw={'autofocus': True})
    username = StringField("Username")
  
    class Meta:
        csrf = False