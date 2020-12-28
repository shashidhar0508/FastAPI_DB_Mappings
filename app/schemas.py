from typing import Optional, List
from pydantic import BaseModel
import datetime

class Stock(BaseModel):
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
    stocks: List[Stock]
