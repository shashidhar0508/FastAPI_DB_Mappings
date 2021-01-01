from typing import Optional, List
from pydantic import BaseModel
import datetime


class StockIn(BaseModel):
    stock_name: str
    buy_price: float
    sell_price: float
    charges: float
    created_on: Optional[datetime.datetime]
    updated_by: str


class PersonCreate(BaseModel):
    name: str
    email: str
    created_on: Optional[datetime.datetime]
    updated_by: str
    stocks: List[StockIn]


class Person(BaseModel):
    name: str
    email: str


class Stock(BaseModel):
    stock_name: str
    buy_price: float
    sell_price: float
    charges: float


class PersonStocks(BaseModel):
    person: Person
    stocks_list: List[Stock]
