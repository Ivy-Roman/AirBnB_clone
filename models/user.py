#!/usr/bin/python3

"""User Module
This module inherits from the BaseModel class.
It contains the user information"""

from models.base_model import BaseModel

class User(BaseModel):
    """User Class
    Attributes:
        email (str): The user email
        password (str): The user password
        first_name (str): The first name of the user
        last_name (str): The last name of the user
        """
    email = ''
    password = ''
    first_name = ''
    last_name = ''