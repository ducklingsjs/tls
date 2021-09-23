"""Team model."""
from . import db


class Team(db.Model):
    """Team model."""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

    @classmethod
    def create(cls, name):
        """Create a team."""
        team = Team(name=name)
        db.session.add(team)
        db.session.commit()

        return team

    @classmethod
    def get_by_id(cls, id):
        """Get by id."""
        return cls.query.filter_by(id=id).first()

    def view(self):
        """Object view."""
        return dict(id=self.id, name=self.name)
