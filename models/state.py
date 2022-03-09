#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy import relationship, backref
import os

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)
    cities = relantionnship("City", cascade="all, delete-orphan",
                            backref="states",
                            passive_deletes=True,
                            single_parent=True)
    if os.getenv("HBNB_TYPE_STROAGE") != "db":
        @property
        def cities(self):
            """returns the list of City instances with state_id equals to the current State.id"""
            from models import storage
            from models import City

            all_objects = storage.all()
            city_lists = []
            for keys, values in all_objects.items():
                if values.state_id == self.id:
                    city_list.append(values)
                    return city_lists
