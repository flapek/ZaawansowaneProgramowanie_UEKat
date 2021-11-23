from flask_restful import Resource
from reositories.movie_repository import parse
from utils.file_reader import read_file
from utils.json_extension import to_json, to_json_string


class MovieController(Resource):
    def get(self):
        return to_json(to_json_string(parse(read_file("movies.csv"))))
