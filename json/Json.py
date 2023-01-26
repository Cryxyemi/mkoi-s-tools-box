import json


class JsonClass:

    def __init__(self, path: str) -> None:
        self.path = path

    def __open_file__(self, mode: str):
        with open(self.path, mode) as f:
            return f

    def get_item(self, name: str):
        file = self.__open_file__('r')
        json_file = json.load(file)

        return json_file[name]

    def to_dict(self):
        file = self.__open_file__('r')
        
        return json.load(file)