from dataclasses import dataclass
from application.candidates.models import Tag
from application.votes.models import Approval, Veto

@dataclass
class APIBase():
    name: str
    url: str
    nominator: str # Username

@dataclass
class APICandidate(APIBase):
    approvals: Approval
    vetoes: Veto
    tags: Tag

@dataclass
class APISelected(APIBase):
    tags: Tag
    time_selected: str
