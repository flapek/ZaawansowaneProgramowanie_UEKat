import json


def to_json_string(list_of_objects: list):
    return json.dumps(
        [o.__dict__() for o in list_of_objects],
        default=lambda obj: obj.__dict__,
    )


def to_json(obj: str) -> any:
    return json.loads(obj)
