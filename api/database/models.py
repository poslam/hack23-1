import enum

from sqlalchemy import TEXT, TIMESTAMP, Boolean, Column, Enum, Integer

from database.database import base


class UserTypes(enum.Enum):
    admin = "admin"
    driver = "driver"
    packer = "packer"


class User(base):
    __tablename__ = "client"

    id = Column(Integer, primary_key=True)

    first_name = Column(TEXT)
    second_name = Column(TEXT)
    third_name = Column(TEXT)

    email = Column(TEXT)

    password = Column(TEXT)
    type = Column(Enum(UserTypes))

    car_num = Column(TEXT)
    active_shift = Column(Boolean, default=False)
    expedition = Column(Integer)


class RefreshTokenStorage(base):
    __tablename__ = "refresh_token_storage"

    id = Column(Integer, primary_key=True)

    refresh_token = Column(TEXT)
    expired = Column(TIMESTAMP)
