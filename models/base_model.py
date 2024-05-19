#!/usr/bin/python3
"""BaseModel class defines common attributes/methods"""

import uuid
from datetime import datetime
import models

time_form = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """Define HBnB Base_Model"""
    def __init__(self, *args, **kwargs):
        """ Initialization of the object/instance attributes """

        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, time_form))
                elif key != "__class__":
                    setattr(self, key, value)
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
            if "created_at" not in kwargs:
                self.created_at = datetime.now()
            if "updated_at" not in kwargs:
                self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ Writing the __str__ method """
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)

    def save(self):
        """ Public instance methods:
            updates the public instance attribute updated_at
            with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ Public instance methods:
            returns a dictionary containing all keys/values
            of __dict__.
        """
        dic_BaseClass = self.__dict__.copy()
        dic_BaseClass["__class__"] = self.__class__.__name__
        dic_BaseClass["created_at"] = self.created_at.isoformat()
        dic_BaseClass["updated_at"] = self.updated_at.isoformat()
        return dic_BaseClass
