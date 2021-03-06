#!/usr/bin/python3
"""
    State Module
"""
from models.base_model import BaseModel


class State(BaseModel):
    """State class

    Attributes:
        name (str): empty string
    """

    name = ""

    def __init__(self, *args, **kwarg):
        """ Method for initialize State Class"""
        super().__init__(*args, **kwargs)
