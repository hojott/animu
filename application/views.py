from flask import render_template, redirect, url_for
from application import app, db, login_required
from application.votes.models import Veto, Approval

@app.route("/")
def index():
    return redirect(url_for("candidates_index"))


@app.route("/administrate/", methods=["GET"])
@login_required(role="ADMIN")
def admin():
    return render_template("/admin.html")

@app.route("/administrate/reset_votes", methods=["POST"])
@login_required(role="ADMIN")
def admin_reset_votes():
    Veto.query.delete()
    Approval.query.delete()
    db.session.commit()
    return redirect(url_for("admin"))