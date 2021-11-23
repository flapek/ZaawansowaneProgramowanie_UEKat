from flask_restful import Resource
from reositories.tag_repository import get_tag_data
from utils.json_extension import to_json, to_json_string


class TagController(Resource):
    def get(self):
        return to_json(to_json_string(get_tag_data()))
