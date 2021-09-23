"""Main."""
import os
from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from app.models import init_app


def create_app(test_config=None):
    """Create Flask app."""
    app = Flask(__name__, instance_relative_config=True)
    db_path = os.path.join(app.instance_path, "db.sqlite")
    app.config.from_mapping(
        SECRET_KEY="dev",
        SQLALCHEMY_DATABASE_URI='sqlite:///' + db_path,
        SQLALCHEMY_TRACK_MODIFICATIONS=False
    )

    api = Api(app)
    CORS(app)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    init_app(app)

    from app.controllers.team import Team
    from app.controllers.user import User
    from app.controllers.rating import Rating
    api.add_resource(Team, '/api/team')
    api.add_resource(User, '/api/user')
    api.add_resource(Rating, '/api/rating')

    return app
