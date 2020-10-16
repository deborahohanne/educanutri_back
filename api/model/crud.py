from sqlalchemy.orm import Session

from . import models, schemas


def get_alimentos_all(db: Session):
    return db.query(models.Alimento).all()


def get_pratos_all(db: Session):
    return db.query(models.Prato).all()


def create_alimento(db: Session, alimento: schemas.AlimentoCreate):
    db_alimento = models.Alimento(**alimento.dict())
    db.add(db_alimento)
    db.commit()
    db.refresh(db_alimento)
    return db_alimento

def create_prato(db: Session, prato: schemas.PratoCreate):
    db_prato = models.Prato(prato.dict())
    db.add(db_prato)
    db.commit()
    db.refresh(db_prato)
    return db_prato
