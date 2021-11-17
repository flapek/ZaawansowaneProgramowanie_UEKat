import json


def to_json(list_of_objects: list):
    obj = [o.__dict__() for o in list_of_objects]

    return json.dumps(obj, default=lambda obj: obj.__dict__)
