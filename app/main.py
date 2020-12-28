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


@app.post("/persons/")
def create_person(
        person: schemas.PersonCreate, db: Session = Depends(get_db)
):
    crud.create_person(db=db, person=person)
    # return crud.create_person(db=db, person=person)
    return {"id":"sdf"}
