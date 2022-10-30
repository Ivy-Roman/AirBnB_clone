#!/usr/bin/python3
"""State Module
This module inherits from BaseModel class.
State mdoule contains the attributes to be assigned
to the states"""

from models.base_model import BaseModel

class State(BaseModel):
    """State Class
    Attributes:
        name (str): The state name
    """
    name = ''