from sqlalchemy.orm import Session
import models
import schemas
from datetime import datetime

def create_person(db: Session, person: schemas.PersonCreate):
    stock_list = person.stocks
    print("stock_list : ",stock_list)
    print("type(stock_list) : ",type(stock_list))
    db_person = models.Person(name=person.name, email=person.email, created_on=datetime.now(),
                              updated_by=person.updated_by)
    db.add(db_person)
    db.commit()
    db.refresh(db_person)
    print("db_person : ",db_person)
    for stock in stock_list:
        print("stock : ", stock)
        print("type(stock) : ", type(stock))
        print("db_person.id : ",db_person.id)
        db_stock = models.Stock(stock_name=stock.stock_name, buy_price=stock.buy_price, sell_price=stock.sell_price,
                                  charges=stock.charges, created_on=datetime.now(),
                              updated_by=stock.updated_by,person_id=db_person.id)
        print("db_stock : ", db_stock)
        print("type(db_stock) : ", type(db_stock))
        db.add(db_stock)
        db.commit()
        db.refresh(db_stock)
        print("db_stock : ",db_stock)
    return db_person
