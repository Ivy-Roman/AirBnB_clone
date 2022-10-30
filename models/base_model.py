#!/usr/bin/python3
"""The Base Model contains instances and methods for other classes"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """BaseModel class definition"""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel object

        Args:
            *args (any): Unused
            **kwargs (dict): Key/value pairs of attributes
        """
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for arg, val in kwargs.items():
                if arg in ('created_at', 'updated_at'):
                    val = datetime.strptime(val, time_format)
                if arg != '__class__':
                    setattr(self, arg, val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """Representation of the class for the user

        Example:
            $ base_model = BaseModel()
            $ print(bm)

            This method prints the content of the BaseModel
            class with this format
            $ [<class name>] (<self.id>) <self.__dict__>
        """
        return '[{0}] ({1}) {2}'.format(
            self.__class__.__name__, self.id, self.__dict__
        )

    def save(self):
        pass
