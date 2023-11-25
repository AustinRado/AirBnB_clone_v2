#!/usr/bin/python3
"""New storage engine"""
try:
    from os import getenv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker, scoped_session
    from models.base_model import BaseModel, Base
    from models.city import City
    from models.amenity import Amenity
    from models.place import Place
    from models.state import State
    from models.review import Review
    from models.user import User
except ImportError as e:
    print(f'Import error', e)

"""Get environment variables"""
database = getenv("HBNB_MYSQL_DB")
user = getenv("HBNB_MYSQL_USER")
host = getenv("HBNB_MYSQL_HOST")
password = getenv("HBNB_MYSQL_PWD")
hbnb_env = getenv("HBNB_ENV")

"""Define a dictionary that maps class names to their corresponding classes"""
classes = {"State": State, "City": City, "User": User,
           "Place": Place, "Review": Review, "Amenity": Amenity}


class DBStorage:
    """
    A class for managing database storage.
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        Intitialise db instance
        """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
                                      user, password, host, database),
                                      pool_pre_ping=True)

        """If running in test env drop all tables"""
        if hbnb_env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query database session
        RETURN: dict
            key = <class-name>.<object-id>
            value = object
        """
        db_obj = {}
        if cls:
            if type(cls) is str and cls in classes:
                for obj in self.__session.query(classes[cls]).all():
                    key = str(obj.__class__.__name__) + "." + str(obj.id)
                    db_obj[key] = obj
        else:
            for class_name, class_type in classes.item():
                for obj in self.__session.query(class_type).all():
                    key = str(class_type.__name__) + "." + str(obj.id)
                    db_obj[key] = obj
        return db_obj

    def new(self, obj):
        """Adds obj to the current session"""
        if obj:
            self.__session.add(obj)

    def save(self):
        """commit changes of current db session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete an obj from current session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """create tables in the db and init current db session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """close current session"""
        self.__session.close()
