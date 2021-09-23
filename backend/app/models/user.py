"""User model."""
from . import db
from werkzeug.security import generate_password_hash


class User(db.Model):
    """User model."""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)

    @classmethod
    def create(cls, name, password):
        """Create a User."""
        user = User(name=name, password=generate_password_hash(password))
        db.session.add(user)
        db.session.commit()

        return user

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get_by_name(cls, name):
        """Get by name."""
        return cls.query.filter_by(name=name).first()

    @classmethod
    def get_by_id(cls, id):
        """Get by id."""
        return cls.query.filter_by(id=id).first()

    def view(self):
        """Object view."""
        return dict(id=self.id, name=self.name)
