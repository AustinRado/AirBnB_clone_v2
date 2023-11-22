#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
try:
    import uuid
    from datetime import datetime
    from models import storage
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy import Column, String, DATETIME
except ImportError as e:
    print(f'Import error', e)

Base = declarative_base()


class BaseModel():

    """
    Attributes
    id : columns, CHAR(60), Not null, PK
    created_at : rep col containing datetime, not null,
                default value = current time (datetime.utnow())
    updated_at : rep col containing datetime, not null,
                default value = current time (datetime.utnow())
    """

    id = Column(String(60),
                nullable=False,
                primary_key=True,
                unique=True)

    created_at = Column(DATETIME,
                        nullable=False,
                        default=datetime.utnow())

    updated_at = Column(DATETIME,
                        nullable=False,
                        default=datetime.utnow())

    """A base class for all hbnb models"""
    def __init__(self, *args, **kwargs):
        """Instantiates a new model"""
        if not kwargs:
            # from . import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

        else:
            for kwarg in kwargs:
                if kwarg in ['created_at','updated_at']:
                    setattr(self, kwarg, datetime.fromisoformat(kwargs[kwarg]))
                elif kwarg != '__class__':
                    setattr(self, kwarg, kwargs[kwarg])

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        # from . import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        for dict in dictionary:
            if type(dictionary[dict]) is datetime:
                dictionary[dict] =  dictionary[dict].isoformat()
        if '_sa_instance_state' in dictionary.keys():
            del(dictionary['_sa_instance_state'])
        return dictionary

    def delete(self):
        """deletes current instance from the storage"""
        storage.delete(self)