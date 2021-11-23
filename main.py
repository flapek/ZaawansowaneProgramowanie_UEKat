from flask import Flask
from flask_restful import Api
from controllers.HelloWorld_API import HelloWorld
from controllers.Movie_API import Movie_API

app = Flask(__name__)
api = Api(app)


api.add_resource(HelloWorld, "/")
api.add_resource(Movie_API, "/movies")

if __name__ == "__main__":
    app.run(debug=True)
