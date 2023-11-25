from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField
from flask_babel import lazy_gettext

class CandidateForm(FlaskForm):
    name = StringField(lazy_gettext("Candidate name"))
    url = StringField(lazy_gettext("Candidate URL, e.g. Aniwave page"))
 
    class Meta:
        csrf = False

class EditForm(FlaskForm):
    name = StringField(lazy_gettext("Candidate name"))
    url = StringField(lazy_gettext("Candidate URL"))
    selected = BooleanField(lazy_gettext("Selected"))
    
    class Meta:
        csrf = False
