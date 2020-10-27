from sqlalchemy.orm import Session

from . import models, schemas


def search_plate(db: Session, tipo: int):
    return db.query(models.Prato).filter(models.Prato.tipo == tipo).all()

def search_food(db: Session, grupo: int):
    return db.query(models.Alimento).filter(models.Alimento.grupo == grupo).all()

def search_creation(db: Session, id_prato: int):
    return db.query(models.Criacao).filter(models.Criacao.id_prato == id_prato).all()

def search_foods(db: Session, id_alimento: int):
    return db.query(models.Alimento).filter(models.Alimento.id == id_alimento).all()