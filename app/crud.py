from sqlalchemy.orm import Session
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


def person_account_db(name, email, db: Session):
    print("name : ", name, " email : ", email)
    person_data = db.query(models.Person).filter(models.Person.name == name,
                                                 models.Person.email == email).first()
    print("person_data : ", person_data)
    person_id = person_data.id
    print("person_id : ", person_id)
    stock_list = db.query(models.Stock).filter(models.Stock.person_id == person_id).all()
    print("stock_list : ", stock_list)
    for stock in stock_list:
        print("stock : ", stock)
    person_stocks = PersonStocks()
    person_stocks.person.name = person_data.name
    person_stocks.person.email = person_data.email
    person_stocks.stocks_list = stock_list

    return stock_list

# def person_account_db(db: Session, stock_input: schemas.StockInput):
#     print("name : ", stock_input.name, " email : ", stock_input.email)
#     person_data = db.query(models.Person).filter(models.Person.name == stock_input.name,
#                                                  models.Person.email == stock_input.email).first()
#     print("person_data : ",person_data)
#     return person_data
