from flask import render_template, request, redirect, url_for

from application import app, db
from application.auth.models import User
from application.votes.models import Veto, Approval
from application.forms import AdminForm

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