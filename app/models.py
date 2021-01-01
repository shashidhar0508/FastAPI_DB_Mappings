from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Float
from sqlalchemy.orm import relationship

from database import Base


class Person(Base):
    __tablename__ = "person"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    created_on = Column(DateTime)
    updated_by = Column(String)

    stock = relationship("Stock", back_populates="owner")

    # def __repr__(self):
    #     return "Person id:% s name:% s email:% s created_on:% s updated_by:% s" % \
    #            (self.id, self.name, self.email, self.created_on, self.updated_by)
    #
    # def __str__(self):
    #     return "From str method of Person: id is % s name is % s email is % s created_on is % s updated_by is % " \
    #         (self.id, self.name, self.email, self.created_on, self.updated_by)


class Stock(Base):
    __tablename__ = "stock"

    id = Column(Integer, primary_key=True, index=True)
    stock_name = Column(String)
    buy_price = Column(Float)
    sell_price = Column(Float)
    charges = Column(Float)
    created_on = Column(DateTime)
    updated_by = Column(String)

    person_id = Column(Integer, ForeignKey("person.id"))
    owner = relationship("Person", back_populates="stock")
