import json
from flask import Flask
from flask_restful import Resource, Api

from utils.file_reader import read_file
from utils.movie_extension import parse
from utils.to_json import to_json

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {"hello": "world"}


class Movie_API(Resource):
    def get(self):
        return to_json(parse(read_file("movies.csv")))


api.add_resource(HelloWorld, "/")
api.add_resource(Movie_API, "/movies")

if __name__ == "__main__":
    app.run(debug=True)
