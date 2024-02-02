from flask_wtf import FlaskForm
from wtforms import StringField
from flask_babel import lazy_gettext
  
class LoginForm(FlaskForm):
    username = StringField(lazy_gettext("Username"), render_kw={'autofocus': True})
  
    class Meta:
        csrf = False

class RegisterForm(FlaskForm):
    name = StringField(lazy_gettext("Display name"), render_kw={'autofocus': True})
    username = StringField(lazy_gettext("Username"))
  
    class Meta:
        csrf = False

class EditForm(FlaskForm):
    name = StringField(lazy_gettext("Display name"), render_kw={'autofocus': True})
    username = StringField(lazy_gettext("Username"))
  
    class Meta:
        csrf = False