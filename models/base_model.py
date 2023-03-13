#!/usr/bin/python3
"""This a basemodel module."""
from datetime import datetime
from uuid import uuid4

import models as md


class BaseModel:
    """This is a class"""

    def __init__(self, *args, **kwargs):
        """constructor."""

        if kwargs is not None and len(kwargs) != 0:
            for key, value in kwargs.items():
                if "__class__" == key:
                    continue
                elif key in ['updated_at', 'created_at']:
                    setattr(self, key, datetime.fromisoformat(value))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            md.storage.new(self)

    def __str__(self):
        """String Representation."""

        return "[{}] ({}) {}".format(
                self.__class__.__name__,
                self.id,
                self.__dict__
        )

    def save(self):
        """Save method."""

        self.updated_at = datetime.now()
        md.storage.save()

    def to_dict(self):
        """to dictionary"""
        result = self.__dict__.copy()
        result['__class__'] = self.__class__.__name__
        result['created_at'] = result['created_at'].isoformat()
        result['updated_at'] = result['updated_at'].isoformat()
        return (result)
