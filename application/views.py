from flask import render_template, request, redirect, url_for

from application import app, db
from application.auth.models import User
from application.votes.models import Veto, Approval
from application.forms import AdminForm

@app.template_filter()
def quote(value):
    return "\"" + value + "\""

# Replace empty strings with the same amount of epsilon characters
@app.template_filter()
def empty_to_epsilon(value):
    if len(value) == 0:
        return "∅"
    return value if value.strip() else "ε" * len(value)

# Takes in a generator
@app.template_filter()
def listify(generator):
    array = list(generator)
    return ", ".join(array)

@app.route("/")
def index():
    return redirect(url_for("candidates_index"))


@app.route("/administrate/", methods=["GET"])
def admin():
    return render_template("/admin.html", form=AdminForm())

@app.route("/administrate/reset_votes", methods=["POST"])
def admin_reset_votes():
    form = AdminForm(request.form)
    
    # Hardcoded username "admin" must exist in database
    admin = User.query.filter_by(username="admin", password=form.adminpass.data).first()
    if not admin:
        return render_template("/admin.html", form=form, error="Wrong admin password")
    
    Veto.query.delete()
    Approval.query.delete()
    db.session.commit()
    return redirect(url_for("admin"))