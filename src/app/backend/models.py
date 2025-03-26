from sqlalchemy import String, Column, Integer

from .database import Database

db = Database()


class User(db.BASE):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    login = Column(String)
    email = Column(String)
    password = Column(String)
    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    photo = Column(String)
    date_reg = Column(String)
