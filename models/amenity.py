#!/usr/bin/python3
"""Amenity Module

This module inherits from the basemodel class.
It contains the attributes to be assigned to the amenities of the place"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity Class
    Attributes:
        name (str): The Amenity name
    """
    name = ''
