from application import db
from application.models import Base

class Approval(Base):
    voter_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    candidate_id = db.Column(db.Integer, db.ForeignKey('candidate.id'), nullable=False)

    def __init__(self, voter_id, candidate_id):
        self.voter_id = voter_id
        self.candidate_id = candidate_id

class Veto(Base):
    voter_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    candidate_id = db.Column(db.Integer, db.ForeignKey('candidate.id'), nullable=False)

    def __init__(self, voter_id, candidate_id):
        self.voter_id = voter_id
        self.candidate_id = candidate_id