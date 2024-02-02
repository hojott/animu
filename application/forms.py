from flask_wtf import FlaskForm
from flask_babel import lazy_gettext
from wtforms import PasswordField
  
class AdminForm(FlaskForm):
    adminpass = PasswordField(lazy_gettext("Admin password"), render_kw={'autofocus': True})
  
    class Meta:
        csrf = False