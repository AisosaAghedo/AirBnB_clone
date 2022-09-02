#!/usr/bin/python3
""" subclass state module """
from models.base_model import BaseModel


class State(BaseModel):
    """subclass state that inherits fromn Basemodel """

    name = ""

    def __init__(*args, **kwargs):
        """ initialisation """
        super().__init__(*args, **kwargs)
