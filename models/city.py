#!/usr/bin/python3
"""City Module

This module inherits from BaseModel class.
It contains the attributes to be assigned
to the class"""

from models.base_model import BaseModel

class City(BaseModel):
    """City Class
    This is the city class
    
    Attributes:
        state_id (str): The UUID of hte state that
            the city belongs to
        name (str): The city name"""
    state_id = ''
    name = ''