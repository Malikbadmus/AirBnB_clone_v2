#!/usr/bin/python3
"""create a unique FileStorage instance for your application"""
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from os import getenv


<<<<<<< HEAD
if getenv("HBNB_TYOE_STORAGE") == "db":
=======
if getenv("HBNB_TYPE_STORAGE") == "db":
>>>>>>> 0d34fe9b6c83ca8f6759dc55e53a0b11486157ef
    storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()
