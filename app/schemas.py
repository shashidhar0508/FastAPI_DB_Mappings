from typing import Optional
from pydantic import BaseModel
import datetime


class PersonCreate(BaseModel):
    name: str
    email: str
    created_on: Optional[datetime.datetime]
    updated_by: str
