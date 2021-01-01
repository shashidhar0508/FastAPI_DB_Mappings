from fastapi import FastAPI
import crud, models, schemas
from database import SessionLocal, engine

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def indexes():
    return {"stock": "213"}


@app.post("/stocks/create_person_stocks")
def create_person_stocks(person: schemas.PersonCreate, db: Session = Depends(get_db)):
    return crud.create_person_stocks_db(db=db, person=person)


@app.get("/stocks/person_account/{name}/{email}")
def person_account(name=str, email=str, db: Session = Depends(get_db)):
    # def person_account(stock_input: schemas.StockInput, db: Session = Depends(get_db)):
    # return crud.person_account_db(db=db, stockInput=stock_input)
    return crud.person_account_db(name, email, db=db)
