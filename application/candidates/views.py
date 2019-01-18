from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user, login_manager

from application import app, db
from application.candidates import models
from application.candidates.models import Candidate
from application.candidates.forms import CandidateForm
from application.candidates.forms import EditForm

from application.votes.models import Approval
from application.votes.models import Veto

from application.auth.models import User

@app.route("/candidates/", methods=["GET"])
@app.route("/candidates", methods=["GET"])
def candidates_index():
    candidates = Candidate.query.all()
    for c in candidates:
        setattr(c, "approval", len(c.approvals))
        setattr(c, "veto", len(c.vetoes))
        displayed_tags = []
        for tag in c.tags:
            displayed_tags.append(tag.name)
        setattr(c, "displayed_tags", displayed_tags)

    candidates = sorted(candidates, key=lambda c: c.approval, reverse=True)
    candidates = sorted(candidates, key=lambda c: c.veto)
    return render_template("candidates/list.html", winning=Candidate.find_winning_candidates(), user=User, candidates=candidates)

@app.route("/candidates/new/")
@login_required
def candidates_form():
    return render_template("candidates/new.html", form=CandidateForm())

@app.route("/candidates/selected/<candidate_id>/", methods=["POST"])
@login_required
def candidates_set_selected(candidate_id):
    candidate = Candidate.query.get(candidate_id)
    candidate.selected = True
    db.session().commit()

    return redirect(url_for("candidates_index"))

@app.route("/candidates/edit/<candidate_id>/", methods=["POST", "GET"])
@login_required
def candidates_edit(candidate_id):
    candidate = Candidate.query.get(candidate_id)
    
    if request.method == "GET":
        return render_template("candidates/edit.html",
        form=EditForm(obj=candidate), candidate=candidate)

    if candidate.nominator_id != current_user.id:
        return render_template("candidates/edit.html", error="You can't edit other people's candidates!",
        form=EditForm(obj=candidate), candidate=candidate)

    form = EditForm(request.form)

    candidate.name = form.name.data
    candidate.selected = form.selected.data
    candidate.url = form.url.data

    db.session.commit()

    return redirect(url_for("candidates_index"))

@app.route("/candidates/delete/<candidate_id>/", methods=["POST"])
@login_required
def candidates_delete(candidate_id):
    candidate = Candidate.query.get(candidate_id)

    if candidate.nominator_id != current_user.id:
        return render_template("candidates/edit.html", error="You can't delete other people's candidates!",
            form=EditForm(obj=candidate), candidate=candidate)

    Approval.query.filter_by(candidate_id=candidate_id).delete()
    Veto.query.filter_by(candidate_id=candidate_id).delete()
    db.session().delete(candidate)
    db.session().commit()

    return redirect(url_for("candidates_index"))

@app.route("/candidates/approved/<candidate_id>/", methods=["POST"])
@login_required
def candidates_set_approved(candidate_id):
    candidate = Candidate.query.get(candidate_id)

    approval = Approval.query.filter_by(candidate_id=candidate_id, voter_id=current_user.id).first()

    if (approval == None):
        new_approval = Approval(current_user.id, candidate_id)
        db.session().add(new_approval)
    else:
        db.session().delete(approval)

    db.session().commit()

    return redirect(url_for("candidates_index"))

@app.route("/candidates/veto/<candidate_id>/", methods=["POST"])
@login_required
def candidates_set_veto(candidate_id):
    candidate = Candidate.query.get(candidate_id)

    veto = Veto.query.filter_by(candidate_id=candidate_id, voter_id=current_user.id).first()

    if (veto == None):
        new_veto = Veto(current_user.id, candidate_id)
        db.session().add(new_veto)
    else:
        db.session().delete(veto)

    db.session().commit()

    return redirect(url_for("candidates_index"))

@app.route("/candidates/", methods=["POST"])
@login_required
def candidates_create():
    form = CandidateForm(request.form)

    if not form.validate():
        return render_template("tasks/new.html", form=form)

    candidate = Candidate(form.name.data)
    candidate.url = form.url.data
    candidate.nominator_id = current_user.id

    db.session().add(candidate)
    db.session().commit()

    return redirect(url_for("candidates_index"))
