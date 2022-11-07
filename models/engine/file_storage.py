#!/usr/bin/python3
"""File storage module.
This module is in charge of storing classes
and managing them
"""

import json
from os import path
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """File Storage Class
    Attributes:
        __file_path (str): This is the path of the JSON file
            where the contents of the __objects variable will be stored
        __objects (dict): This stores all the instance data
        """
    __file_path = 'objects.json'
    __objects = {}

    def all(self):
        """Gets the __objects info
        Returns the content of the __objects class attribute"""
        return self.__objects

    def new(self, object):
        """Saves a new object in the __objects class attribute
        Args:
            object (inst): The object to add in the __Objects class attibute
        Sets in the __objects class attribute, the instance data with a key
        as <object class name>.id"""
        key = object.__class__.__name__ + '.' + object.id
        self.__objects[key] = object

    def save(self):
        """Serializes the content of __objects class attribute. The
        content of __objects class attribute will be serialised to
        the path of the __file_path class attribute in JSON format
        with the created_at and updated_at formatted"""
        json_dict = {}
        for key, value in self.__objects.items():
            json_dict[key] = value.to_dict()
        with open(self.__file_path, mode='w', encoding='utf-8') as f:
            f.write(json.dumps(json_dict))

    def reload(self):
        """Deserializes the JSON file in __file_path class attribute
        if the file on __file_path class attribute exists, each object on
        the file will be deserialised and appended to the __objects class
        attribute like an instance with the object data"""
        if path.exists(self.__file_path):
            with open(self.__file_path, mode='r', encoding='utf-8') as f:
                json_dict = json.loads(f.read())
                for key, value in json_dict.items():
                    self.__objects[key] = eval(value['__class__'])(**value)
