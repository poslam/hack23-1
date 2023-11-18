from database.database import base
from sqlalchemy import (
    TIMESTAMP,
    Double,
    Enum,
    Column,
    ForeignKey,
    Integer,
    TEXT,
    String,
)
import enum

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