#!/usr/bin/python3
""" File storage module """
import json
from models.base_model import BaseModel


class FileStorage:
    """ class FileStorage """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """  returns the dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file """
        to_dict = {}
        for key, obj in FileStorage.__objects.items():
            to_dict[key] = obj.to_dict()

        with open(FileStorage.__file_path, 'w', encoding="UTF-8") as file:
            json.dump(to_dict, file)

    def reload(self):
        """ deserializes the JSON file to __objects """
        try:
            with open(FileStorage.__file_path, 'r') as f:
                load = json.load(f)

            new_dict = {}
            for key, value in load.items():
                obj = BaseModel(**value)
                new_dict[key] = obj

            FileStorage.__objects = new_dict

        except FileNotFoundError:
            return
