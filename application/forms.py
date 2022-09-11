from flask_wtf import FlaskForm
from wtforms import PasswordField
  
class AdminForm(FlaskForm):
    adminpass = PasswordField("Admin password", render_kw={'autofocus': True})
  
    class Meta:
        csrf = False