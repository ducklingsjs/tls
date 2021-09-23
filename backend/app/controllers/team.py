"""Team controller."""
from flask import request
from flask_restful import Resource
from app.models.team import Team as TeamModel


class Team(Resource):
    """Team."""

    def get(self):
        """Index."""
        teams = TeamModel.get_all()

        return [team.view() for team in teams]

    def post(self):
        """Create team."""
        data = request.get_json(force=True)
        team = TeamModel.create(name=data["name"])

        return team.view()
