from flask import Flask
from flask_restful import Api
from controllers.HelloWorldController import HelloWorldController
from controllers.LinksController import LinksController

from controllers.MovieController import MovieController


app = Flask(__name__)
api = Api(app)


api.add_resource(HelloWorldController, "/")
api.add_resource(MovieController, "/movies")
api.add_resource(LinksController, "/links")

if __name__ == "__main__":
    app.run(debug=True)
