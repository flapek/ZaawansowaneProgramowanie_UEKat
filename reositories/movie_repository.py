import csv
from io import TextIOWrapper
from models.Movie import Movie


def parse(wrapper: TextIOWrapper) -> list:
    reader = csv.reader(wrapper, delimiter=",")
    next(reader)
    return [Movie(int(row[0]), row[1], row[2]) for row in reader]
