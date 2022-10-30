#!/usr/bin/python3
"""Review Module
This module inherits from BaseModel class.
It contains the attributes to be assigned
to the reviews created by the users"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Review Class
    Attributes:
        place_id (str): The UUID of the place the reiew belongs to
        user_id (str): The UUID of the user that made the review
        text (str): The message that the user wrote about the place
        """
    place_id = ''
    user_id = ''
    text = ''
