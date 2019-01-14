from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField
  
class LoginForm(FlaskForm):
    username = StringField("Username", render_kw={'autofocus': True})
    password = PasswordField("Password")
  
    class Meta:
        csrf = False

class RegisterForm(FlaskForm):
    name = StringField("Display name", render_kw={'autofocus': True})
    username = StringField("Username")
    password = PasswordField("Password")
    pw_check = PasswordField("Repeat password")
  
    class Meta:
        csrf = False

class EditForm(FlaskForm):
    name = StringField("Display name", render_kw={'autofocus': True})
    username = StringField("Username")
    password_old = PasswordField("Old password")
    password_new = PasswordField("New password")
    password_check = PasswordField("Repeat new password")
  
    class Meta:
        csrf = False