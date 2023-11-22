#!/usr/bin/python3
""" City Module for HBNB project """
try:
    from models.base_model import BaseModel, Base
    from models import storage
    from sqlalchemy import Column, String, ForeignKey
    from sqlalchemy.orm import relationship
except ImportError as e:
    print(f'Import error', e)


class City(BaseModel, Base):

    """
    The city class, contains state ID and name
    ATTRIBUTES
    __tablename__ = 'cities'
    name = rep
            COL string(128)
            nullable=False
    state_id = rep
                Columns: String(60)
                nullable=False
                FK to states.id
    """

    __tablename__ = 'cities'
    name = Column(String(128),
                  nullable=False)

    state_id = Column(String(128),
                      ForeignKey('state_id'),
                      nullable=False)
    state_id = ""
    name = ""
