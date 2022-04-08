#!/usr/bin/python3
""" State Module for HBNB project """

from models.base_model import Base, BaseModel
from sqlalchemy import Column, String
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
            """
            returns the list of City instances with 
            state_id equals to the current State.id
            """
            from models import storage
            from models.city import City

            all_objects = storage.all(City)
            city_list = []
            for key, val in all_objects.items():
                if val.state_id == self.id:
                    city_list.append(val)
            return city_list
