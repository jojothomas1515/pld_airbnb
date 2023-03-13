#!/usr/bin/python3
"""File Storage module."""
import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """file storage class."""
    md_dic = {
        'BaseModel': BaseModel,
        'User': User,
    }
    __file_path = "file.json"
    __objects = dict()

    def all(self):
        """all method."""

        return self.__objects

    def new(self, obj):
        """new object."""

        key = ".".join(
                (obj.__class__.__name__, obj.id)
        )
        self.__objects[key] = obj

    def save(self):
        """saves object to file"""

        m_dict = {k: v.to_dict() for k, v in self.__objects.items()}

        with open(self.__file_path, 'w', encoding='utf-8') as fp:
            json.dump(m_dict, fp)

    def reload(self):
        """reload."""

        try:
            with open(self.__file_path, 'r', encoding='utf-8') as fp:
                data: dict = json.load(fp)

            for items in data.values():
                obj = eval(items['__class__'])
                self.new(obj(**items))
        except (FileNotFoundError, FileExistsError):
            pass

    def destroy(self, key):
        del self.__objects[key]
        self.save()
