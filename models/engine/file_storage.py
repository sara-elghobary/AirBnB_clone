#!/usr/bin/python3
"""File Storage Module
This module is in charge of the storage of the
classes and their management.
"""
import json
from models.base_model import BaseModel
from os import path
from models.user import User

class FileStorage:
    """it Serialize instances to a JSON file and deserialize JSON file to instances."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return self.__objects
    
    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file."""
        s_obj = {}
        for key, obj in self.__objects.items():
            s_obj[key] = obj.to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(s_obj, file)

    def reload(self):
        """Deserialize the JSON file to __objects."""
        if path.exists(self.__file_path):
            with open(self.__file_path, mode='r', encoding='utf-8') as f:
                json_dict = json.loads(f.read())
                for k, v in json_dict.items():
                    cls_name = v.pop('__class__')
                    if cls_name == 'User':
                        self.__objects[k] = User(**v)
                    elif cls_name == 'BaseModel':
                        self.__objects[k] = BaseModel(**v)
