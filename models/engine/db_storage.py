#!/usr/bin/python3
"""New storage engine"""
try:
    from models.base_model import Base
    from models.city import City
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker, scoped_session
    from os import getenv
except ImportError as e:
    print(f'Import error', e)


class DBStorage:
    """
    
    """
    __engine = None
    __session = None

    def __init__(self):
        self.__engine

