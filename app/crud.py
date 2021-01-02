from sqlalchemy.orm import Session
from sqlalchemy import func
import models
import schemas
from datetime import datetime
from schemas import PersonStocks


def create_person_stocks_db(db: Session, person: schemas.PersonCreate):
    stock_list = person.stocks
    print("stock_list : ", stock_list)
    print("type(stock_list) : ", type(stock_list))
    db_person = models.Person(name=person.name, email=person.email, created_on=datetime.now(),
                              updated_by=person.updated_by)
    db.add(db_person)
    db.commit()
    db.refresh(db_person)
    print("db_person : ", db_person)
    for stock in stock_list:
        print("stock : ", stock)
        print("type(stock) : ", type(stock))
        print("db_person.id : ", db_person.id)
        db_stock = models.Stock(stock_name=stock.stock_name, buy_price=stock.buy_price, sell_price=stock.sell_price,
                                charges=stock.charges, created_on=datetime.now(),
                                updated_by=stock.updated_by, person_id=db_person.id)
        print("db_stock : ", db_stock)
        print("type(db_stock) : ", type(db_stock))
        db.add(db_stock)
        db.commit()
        db.refresh(db_stock)
        print("db_person : ", db_person)
    return {"status": "success"}


def person_account_db(name, count, db: Session):
    person_data_list = db.query(models.Person).filter(models.Person.updated_by == name).order_by(func.random()) \
        .limit(count).all()
    print("person_data_list : ", person_data_list)
    person_stock_list = []
    for person_data in person_data_list:
        person1 = {'name': person_data.name, 'email': person_data.email}
        person_id = person_data.id
        stock_list = db.query(models.Stock).filter(models.Stock.person_id == person_id).all()
        stock_lists1 = []
        for stock in stock_list:
            each_stock = {'stock_name': stock.stock_name, 'buy_price': stock.buy_price, 'sell_price': stock.sell_price,
                          'charges': stock.charges}
            stock_lists1.append(each_stock)
        print("stock_lists1 : ", stock_lists1)
        person_stocks = PersonStocks(person=person1, stocks_list=stock_lists1)
        person_stock_list.append(person_stocks)
    return person_stock_list
