#!/usr/bin/python3
import json
from models.base_model import BaseModel


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        to_dict = {}
        for key, obj in FileStorage.__objects.items():
            to_dict[key] = obj.to_dict()

        with open(FileStorage.__file_path, 'w', encoding="UTF-8") as file:
            json.dump(to_dict, file)

    def reload(self):
        try:
            with open(FileStorage.__file_path, 'r') as f:
                load = json.load(f)

            new_dict = {}
            for key, value in load.items():
                obj = BaseModel(**value)
                new_dict[key] = obj

        except FileNotFoundError:
            pass
