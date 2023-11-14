#!/usr/bin/python3
"""lockedclass module"""
import json


class Base:
    """base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """init function"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """list dicts to json string"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """from json to string"""
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """save to file function"""
        out_json = [obj.to_dictionary() for obj in list_objs]
        with open(f'{cls.__name__}.json', 'w') as f:
            f.write(Base.to_json_string(out_json))

    @classmethod
    def create(cls, **dictionary):
        """create method of the base class"""
        if dictionary:
            if cls.__name__ == "Rectangle":
                instance = cls(2, 2, 3)
            else:
                instance = cls(1, 4)
            instance.update(**dictionary)
            return instance

    @classmethod
    def load_from_file(cls):
        """load from file to create an instance"""
        filename = f'{cls.__name__}.json'
        try:
            with open(filename) as f:
                dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in dicts]
        except IOError:
            return []
