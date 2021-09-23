"""Team controller."""
from flask_restful import Resource, abort
from app.models.result import Result as ResultModel
from app.models.rating import Rating
from app.models.team import Team


class Result(Resource):
    """Result."""

    def get(self):
        """Index."""
        results = ResultModel.get_all()
        return [result.view() for result in results]

    def post(self):
        """Compute resutls."""
        teams = Team.get_all()
        results = ResultModel.get_all()
        if len(results) > 0:
            abort(406, message="Can't compute any more!")

        ratings = Rating.get_all()
        if len(ratings) <= 0:
            abort(406, message="Can't compute with no ratings!")

        if len(ratings) != 20:
            abort(406, message="We're not done yet!")

        for team in teams:
            total = 0
            for rating in ratings:
                if rating.team.id == team.id:
                    total += rating.cat_works
                    total += rating.cat_impressive
                    total += rating.cat_inovative
                    total += rating.cat_topic
                    total += rating.cat_looks
                    total += rating.cat_functionality
                    total += rating.cat_magic

            ResultModel.create(team=team, total=total)

        return {}
