#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Amenity Module

This Module inherits from BaseModel class.
Amenity Module contains the name attributes.
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity Class

    Attributes:
        name (str): The Amenity name

    """
    name = ''
