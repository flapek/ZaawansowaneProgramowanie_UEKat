from flask_restful import Resource
from reositories.link_repository import get_link_data
from utils.json_extension import to_json, to_json_string


class LinksController(Resource):
    def get(self):
        return to_json(to_json_string(get_link_data()))
