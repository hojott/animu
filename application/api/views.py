from flask import jsonify
from application import app
from application.api.utils import parse_candidates, parse_selections

from application.candidates.models import Candidate

@app.route("/api/candidates", methods=["GET"])
def api_candidates():
    candidates = Candidate.query.filter_by(selected=False).all()
    candidates = sorted(candidates, key=lambda candidate: len(candidate.approvals), reverse=True)
    candidates = sorted(candidates, key=lambda candidate: len(candidate.vetoes))

    return jsonify(parse_candidates(candidates))

@app.route("/api/selected", methods=["GET"])
def api_selected():
    candidates = Candidate.query.filter_by(selected=True).all()
    candidates = sorted(candidates, key=lambda candidate: candidate.date_modified)

    return jsonify(parse_selections(candidates))
