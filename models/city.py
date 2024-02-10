#!/usr/bin/python3
"""City Module

This Module inherits from BaseModel class.
City Module contains the state_id and name attributes.

"""

from models.base_model import BaseModel


class City(BaseModel):
    """City Class

    This is the City Class 

    Attributes:
        state_id (str): The UUID of the State the City belongs to
        name (str): The City name

    """
    state_id = ''
    name = ''
