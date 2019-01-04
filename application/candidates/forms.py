from flask_wtf import FlaskForm
from wtforms import StringField

class CandidateForm(FlaskForm):
    name = StringField("Candidate name")
    url = StringField("Candidate url, e.g. IMDB page")
 
    class Meta:
        csrf = False