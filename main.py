from flask import Flask
from flask_restful import Api
from controllers.HelloWorldController import HelloWorldController
from controllers.LinksController import LinksController
from controllers.RatingController import RatingController
from controllers.TagController import TagController

from controllers.MovieController import MovieController


app = Flask(__name__)
api = Api(app)


api.add_resource(HelloWorldController, "/")
api.add_resource(MovieController, "/movies")
api.add_resource(LinksController, "/links")
api.add_resource(RatingController, "/ratings")
api.add_resource(TagController, "/tags")

if __name__ == "__main__":
    app.run(debug=True)
