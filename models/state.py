#!/usr/bin/python3
""" State Module for HBNB project """
try:
    from models.base_model import BaseModel, Base
    from models import storage
    from models.city import City
    from sqlalchemy import Column, String, ForeignKey
    from sqlalchemy.orm import relationship
except ImportError as e:
    print(f'Import error', e)


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128),
                  nullable=False)
    cities = relationship('City', backref='state',
                          cascade='all, delete, delete-orphan')
    name = ""
