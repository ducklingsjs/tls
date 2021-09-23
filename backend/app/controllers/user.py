"""Team controller."""
from flask import request
from flask_restful import Resource, abort
from werkzeug.security import check_password_hash
from app.models.user import User as UserModel


class User(Resource):
    """User."""

    def post(self):
        """Login."""
        data = request.get_json(force=True)
        user = UserModel.get_by_name(name=data["name"])

        if user is None or not check_password_hash(user.password,
                                                   data["password"]):
            abort(404, message="No such user or password inccorect.")

        return user.view()
