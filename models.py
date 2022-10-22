from sqlalchemy.sql.expression import null
from turtle import st
from database import Base
from sqlalchemy import String, Integer, Column, Text,Boolean

class Canciones (Base):
    __tablename__ = 'Canciones'
    id=Column(Integer,primary_key=True)
    name=Column(String(255),nullable=False,unique = True)
    description=Column(Text)
    artist=Column(String(350),nullable=False,unique=True)
    duration=Column(Integer)
    extension=Column(String(255),nullable=False,unique = True)
    album=Column(String(255),nullable=False,unique = True)
    anio=Column(Integer)

    def __repr__(self):
        return f"<Canciones name={self.name} description={self.description}>"