#!/usr/bin/python3
""" subclass User module """
from models.base_model import BaseModel


class User(BaseModel):
    """ subclass user that inherits from Basemodel"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
