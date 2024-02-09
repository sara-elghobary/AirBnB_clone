#!/usr/bin/python3
"""Initializes a variable `storage` to create a
unique `FileStorage` instance for the HBNB application.

"""
#from .engine.file_storage import FileStorage
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
