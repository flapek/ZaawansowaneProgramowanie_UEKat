from flask_restful import Resource
from reositories.movie_repository import get_movie_data
from utils.json_extension import to_json, to_json_string


class MovieController(Resource):
    def get(self):
        return to_json(to_json_string(get_movie_data()))
