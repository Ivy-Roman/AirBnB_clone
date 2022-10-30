#!/usr/bin/python3
🎶"""Place Module
This module inherits from the BaseModel class.
It contains the attributes to be assigned to the place created"""

from models.base_model import BaseModel


class Place(BaseModel):
    """Place Class
    Attributes:
        city_id (str): The UUID of the city that the place is located in
        user_id (str): The UUID of the user of the place
        name (str): The name of the place
        description (str): The description of the place
        number_rooms (int): The number of rooms in the place
        number_bathrooms (int): The number of bathrooms in the place
        max_guest (int): The max_number of guest in the place
        price_by_night (int): The price per night
        latitude (float): The latitude of the place
        longitude (float): The longitude of the place
        amenity_ids: A list that contains all the amenities in the place
        """
    city_id = ''
    user_id = ''
    name = ''
    description = ''
    number_rooms = 0
    number_bathrooms = ''
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_id = []
