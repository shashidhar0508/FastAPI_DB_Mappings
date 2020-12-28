from sqlalchemy.orm import Session
import models
import schemas


def create_person(db: Session, person: schemas.PersonCreate):
    db_person = models.Person(name=person.name, email=person.email, created_on=person.created_on,
                              updated_by=person.updated_by)
    db.add(db_person)
    db.commit()
    db.refresh(db_person)
    return db_person
    return db_person
