import csv
from io import TextIOWrapper
from models.Movie import Movie


def parse(wrapper: TextIOWrapper) -> list:
    result = []
    reader = csv.reader(wrapper, delimiter=",")
    next(reader)
    for row in reader:
        result.append(Movie(int(row[0]), row[1], row[2]))
    return result
