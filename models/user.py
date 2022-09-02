#!/usr/bin/python3
""" subclass User module """
from models.base_model import BaseModel


class User(BaseModel):
    """ subclass user that inherits from Basemodel"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(*args, **kwargs):
        """ initialization of the class """
        super().__init__(*args, **kwargs)
