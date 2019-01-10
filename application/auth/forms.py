from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField
  
class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")
  
    class Meta:
        csrf = False

class RegisterForm(FlaskForm):
    name = StringField("Display name")
    username = StringField("Username")
    password = PasswordField("Password")
    pw_check = PasswordField("Repeat password")
  
    class Meta:
        csrf = False