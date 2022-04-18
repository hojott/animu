from dataclasses import dataclass
from application.candidates.models import Tag
from application.votes.models import Approval, Veto

@dataclass
class APICandidate():
    name: str
    selected: bool
    url: str
    nominator: str # Username
    approvals: Approval
    vetoes: Veto
    tags: Tag
