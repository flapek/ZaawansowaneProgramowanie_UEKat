from flask_restful import Resource
from repositories.movie_repository import get_movies


class Movie_API(Resource):
    def get(self):
        return get_movies()
