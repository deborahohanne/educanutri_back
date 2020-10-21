from sqlalchemy.orm import Session

from . import models, schemas


def search_plate(db: Session, tipo: int):
    return db.query(models.Prato).filter(models.Prato.tipo == tipo).all()