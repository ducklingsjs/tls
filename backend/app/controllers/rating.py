"""Rating controller."""
from flask import request
from flask_restful import Resource, abort
from app.models.user import User as UserModel
from app.models.team import Team as TeamModel
from app.models.rating import Rating as RatingModel


class Rating(Resource):
    """Rating."""

    def post(self):
        """Create a ating."""
        data = request.get_json(force=True)
        user = UserModel.get_by_id(id=data["grader_id"])
        team = TeamModel.get_by_id(id=data["team_id"])

        if user is None:
            abort(403, message="No such user.")

        if team is None:
            abort(403, message="No such team.")

        r = RatingModel.create(team=team, grader=user,
                               cat_works=data["cat_works"],
                               cat_impressive=data["cat_impressive"],
                               cat_topic=data["cat_topic"],
                               cat_looks=data["cat_looks"],
                               cat_magic=data["cat_magic"],
                               cat_functionality=data["cat_functionality"],
                               cat_inovative=data["cat_inovative"],
                               )

        return r.view()
