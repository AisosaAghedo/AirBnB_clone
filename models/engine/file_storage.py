#!/usr/bin/python3
""" File storage module """
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import os


class FileStorage:
    """ class FileStorage """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """  returns the dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, str(obj.id))
        FileStorage.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file """
        to_dict = {}
        for key, obj in FileStorage.__objects.items():
            to_dict[key] = obj.to_dict()

        with open(FileStorage.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(to_dict, f)

    def reload(self):
        """ deserializes the JSON file to __objects """
        if (os.path.isfile(FileStorage.__file_path)):
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as f:
                load = json.load(f)
                for key, value in load.items():
                    FileStorage.__objects[key] = eval(
                        value['__class__'])(**value)
