#!/usr/bin/python3
""" module of subclass Amenity """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ subclass Amenity that inherits from class
    BaseModel """

    name = ""

    def __init__(*args, **kwargs):
        """ initialisation """
        super().__init__(*args, **kwargs)
