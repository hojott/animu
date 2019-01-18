from application import db
from application.models import Base

class User(Base):

    __tablename__ = "account"

    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)

    nominations = db.relationship("Candidate", backref='account', lazy=True, cascade="all, delete-orphan")
    approvals = db.relationship("Approval", cascade="all, delete-orphan")
    vetoes = db.relationship("Veto", cascade="all, delete-orphan")

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
  
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def roles(self):
        if self.username == "admin":
            return ["ADMIN"]
        else:
            return []