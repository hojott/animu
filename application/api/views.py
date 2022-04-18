from flask import jsonify
from application import app
from application.api.models import APICandidate
from application.auth.models import User

from application.candidates.models import Candidate

@app.route("/api/candidates", methods=["GET"])
def api_candidates():
    raw_candidates: Candidate = Candidate.query.filter_by(selected=False).all()
    raw_candidates = sorted(raw_candidates, key=lambda candidate: len(candidate.approvals), reverse=True)
    raw_candidates = sorted(raw_candidates, key=lambda candidate: len(candidate.vetoes))

    candidates: APICandidate = []
    
    for rc in raw_candidates:
      candidates.append(
        APICandidate(
          rc.name,
          rc.selected,
          rc.url,
          User.query.get(rc.nominator_id).name,
          [User.query.get(approval.voter_id).name for approval in rc.approvals],
          [User.query.get(veto.voter_id).name for veto in rc.vetoes],
          [tag.name for tag in rc.tags]
        )
      )

    return jsonify(candidates)

