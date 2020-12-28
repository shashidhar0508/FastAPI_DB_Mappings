from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Float
from sqlalchemy.orm import relationship

from database import Base


class Person(Base):
    __tablename__ = "person"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    created_on = Column(DateTime, unique=True, index=True)
    updated_by = Column(String, unique=True, index=True)

    stock = relationship("Stock", back_populates="owner")


class Stock(Base):
    __tablename__ = "stock"

    id = Column(Integer, primary_key=True, index=True)
    stock_name = Column(String, unique=True, index=True)
    buy_price = Column(Float, unique=True, index=True)
    sell_price = Column(Float, unique=True, index=True)
    charges = Column(Float, unique=True, index=True)
    created_on = Column(DateTime, unique=True, index=True)
    updated_by = Column(String, unique=True, index=True)

    person_id = Column(Integer, ForeignKey("person.id"))
    owner = relationship("Person", back_populates="stock")
