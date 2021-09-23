"""Rating model."""
from . import db


class Rating(db.Model):
    """Rating model."""

    id = db.Column(db.Integer, primary_key=True)
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'),
                        nullable=False)
    team = db.relationship('Team',
                           backref=db.backref('team', lazy=True))
    grader_id = db.Column(db.Integer, db.ForeignKey('user.id'),
                          nullable=False)
    grader = db.relationship('User',
                             backref=db.backref('user', lazy=True))

    cat_works = db.Column(db.Integer, nullable=False)
    cat_impressive = db.Column(db.Integer, nullable=False)
    cat_inovative = db.Column(db.Integer, nullable=False)
    cat_topic = db.Column(db.Integer, nullable=False)
    cat_looks = db.Column(db.Integer, nullable=False)
    cat_functionality = db.Column(db.Integer, nullable=False)
    cat_magic = db.Column(db.Integer, nullable=False)

    __table_args__ = (
        db.UniqueConstraint('team_id', 'grader_id'),
    )

    @classmethod
    def create(cls, team, grader, cat_works, cat_impressive, cat_topic,
               cat_looks, cat_functionality, cat_magic, cat_inovative):
        """Create a rating."""
        rating = Rating(team=team, grader=grader, cat_works=cat_works,
                        cat_impressive=cat_impressive, cat_topic=cat_topic,
                        cat_looks=cat_looks, cat_magic=cat_magic,
                        cat_functionality=cat_functionality,
                        cat_inovative=cat_inovative)
        try:
            db.session.add(rating)
            db.session.commit()
        except:
            db.session.rollback()
            raise

        return rating

    @classmethod
    def get_all(cls):
        """Get all."""
        return cls.query.all()

    def view(self):
        """Object view."""
        return dict(id=self.id, team=self.team.name, grader=self.grader.name)
