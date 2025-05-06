from dataclasses import dataclass


@dataclass
class Stato:
    StateAbb: str
    CCode: int
    StateNme: str

    def __hash__(self):
        hash(self.StateNme)

    def __eq__(self, other):
        return self.CCode == other.CCode

    def __str__(self):
        return self.StateNme