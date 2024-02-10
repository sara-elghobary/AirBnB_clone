#!/usr/bin/python3
"""State Module

This Module inherits from BaseModel class.
State Module contains the name attributes

"""

from models.base_model import BaseModel


class State(BaseModel):
    """State Class

    Attributes:
        name (str): The State name

    """
    name = ''
