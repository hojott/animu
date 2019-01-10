from application import db
from application.models import Base
from application.votes.models import Approval

class Candidate(Base):
    name = db.Column(db.String(144), nullable=False)
    selected = db.Column(db.Boolean, nullable = False)
    url = db.Column(db.String(144), nullable=False)
    nominator_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    votes = db.relationship("Approval", backref='approval', lazy=True)

    def __init__(self, name):
        self.name = name
        self.selected = False
        self.url = ""

    @staticmethod
    def find_winning_candidates():
        candidates = Candidate.query.all()
        winners = []
        max_score = -1
        for c in candidates:
            score = Approval.query.filter_by(candidate_id=c.id).count()
            if score > max_score:
                winners.clear()
                winners.append(c.name)
                max_score = score
            elif score == max_score:
                winners.append(c.name)
        
        return winners
