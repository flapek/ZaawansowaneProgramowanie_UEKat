from io import TextIOWrapper
from models.Movie import Movie
import csv


def parse(wrapper: TextIOWrapper) -> list:
    result = []
    reader = csv.reader(wrapper, delimiter=",")
    for row in reader:
        result.append(Movie(row[0], row[1], row[2]))
    return result

