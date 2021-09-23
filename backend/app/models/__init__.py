"""Models."""
import click
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask.cli import with_appcontext
from flask import current_app

db = SQLAlchemy()
migrate = Migrate()


@click.command("init-db")
@with_appcontext
def init_db_command():
    """Clear existing data and create new tables."""
    db.create_all(app=current_app)

    from app.models.user import User
    User.create(name="tickle@me", password="tickle@me")
    User.create(name="bambi", password="bambi123")
    User.create(name="safo", password="safo123")
    User.create(name="andreicek", password="safo123")

    from app.models.team import Team
    Team.create(name="YOLO")
    Team.create(name="baby")
    Team.create(name="vegan")
    Team.create(name="subway")
    Team.create(name="organic")

    click.echo("Initialized the database.")


def init_app(app):
    """Register database functions with the Flask app."""
    db.init_app(app)
    migrate.init_app(app, db)
    app.cli.add_command(init_db_command)
