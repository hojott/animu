from application import db
from application.models import Base
from application.votes.models import Approval, Veto

class Candidate(Base):
    name = db.Column(db.String(144), nullable=False)
    selected = db.Column(db.Boolean, nullable = False)
    url = db.Column(db.String(144), nullable=False)
    nominator_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    approvals = db.relationship("Approval", backref='approval', lazy=True)
    vetoers = db.relationship("Veto", backref='veto', lazy=True)
    tags = db.relationship('Tag', secondary=tags, lazy='subquery',
        backref=db.backref('pages', lazy=True))

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
            if Veto.query.filter_by(candidate_id=c.id).count() != 0:
                continue
            score = Approval.query.filter_by(candidate_id=c.id).count()
            if score > max_score:
                winners.clear()
                winners.append(c.name)
                max_score = score
            elif score == max_score:
                winners.append(c.name)
        
        return winners

class Tag(db.Model):
    name = db.Column(db.String(50), primary_key=True)

class Tags(db.Model):
    tag_name = db.Column('tag_name', db.Integer, db.ForeignKey('tag.name'), primary_key=True)
    candidate_id = db.Column('candidate_id', db.Integer, db.ForeignKey('candidate.id'), primary_key=True)