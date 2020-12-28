from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Float
from sqlalchemy.orm import relationship

from database import Base


class Person(Base):
    __tablename__ = "person"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    created_on = Column(DateTime, index=True)
    updated_by = Column(String, index=True)

    stock = relationship("Stock", back_populates="owner")


class Stock(Base):
    __tablename__ = "stock"

    id = Column(Integer, primary_key=True, index=True)
    stock_name = Column(String)
    buy_price = Column(Float, index=False)
    sell_price = Column(Float)
    charges = Column(Float)
    created_on = Column(DateTime, index=False)
    updated_by = Column(String, index=False)

    person_id = Column(Integer, ForeignKey("person.id"))
    owner = relationship("Person", back_populates="stock")
