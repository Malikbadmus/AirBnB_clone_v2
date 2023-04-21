#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from sqlalchemy import String, Column, ForeignKey
from sqlalchemy.orm import relationship
import models
from models.base_model import BaseMode
from models.city import City


class State(BaseModel):
    """ State class """
    name = ""

    def __init__(self, obj_dict=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if obj_dict:
            for k, v in obj_dict.items():
                setattr(self, k, v)
        else:
            return

    __tablenmae__ = 'states'
    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', backref='state',
                              cascade='all, delete-orphan')
    else:
        @property
        def cities(self):
            """Attribute: Getter in case of file storage"""
            return [city for city in models.storage.all(City).values()
                    if city.state_id == self.id]
