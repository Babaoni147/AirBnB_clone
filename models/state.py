#!/usr/bin/python3
""" class State that inherits from BaseModel """
from models.base_model import BaseModel


class State(BaseModel):
    """
        Definning the State class that inherits from BaseModel
        Public class attributes:
            name (str): The name of the state.
    """
    name = ""
