from utils.file_reader import read_file
from utils.movie_extension import parse
from utils.json_extension import to_json, to_json_string


def get_movies_data():
    return parse(read_file("movies.csv"))


def get_movies():
    return to_json(to_json_string(get_movies_data))
