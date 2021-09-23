"""User model."""
from . import db


class Result(db.Model):
    """Result model."""

    id = db.Column(db.Integer, primary_key=True)
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'),
                        nullable=False)
    team = db.relationship('Team',
                           backref=db.backref('team_result', lazy=True))
    total = db.Column(db.Integer, nullable=False)

    @classmethod
    def create(cls, team, total):
        """Create a Rating."""
        result = Result(team=team, total=total)
        db.session.add(result)
        db.session.commit()

        return result

    @classmethod
    def get_all(cls):
        """Get all."""
        return cls.query.all()

    def view(self):
        """Object view."""
        return dict(id=self.id, team=self.team.name, total=self.total)
