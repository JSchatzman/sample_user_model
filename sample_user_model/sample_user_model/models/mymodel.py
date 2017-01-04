from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    Unicode
)

from .meta import Base


class MyModel(Base):
    __tablename__ = 'models'
    id = Column(Integer, primary_key=True)
    name = Column(Unicode)
    value = Column(Integer)


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(Unicode)
    firstname = Column(Unicode)
    lastname = Column(Unicode)
    email = Column(Unicode)
    password = Column(Unicode)
    favoritefood = Column(Unicode)

Index('my_index', MyModel.name, unique=True, mysql_length=255)
Index('user_index', User.username, unique=True, mysql_length=255)

