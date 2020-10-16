from sqlalchemy.orm import Session

from . import models, schemas


def get_foods_all(db: Session):
    return db.query(models.Alimento).all()


def get_food_by_id(db: Session, alimento_id: int):
    alimento = db.query(models.Alimento).filter(models.Alimento.id == alimento_id).first()
    return alimento


def get_plates_all(db: Session):
    return db.query(models.Prato).all()


def get_plate_by_id(db: Session, prato_id: int):
    prato = db.query(models.Prato).filter(models.Prato.id == prato_id).first()
    return prato


def create_food(db: Session, alimento: schemas.AlimentoCreate):
    db_alimento = models.Alimento(**alimento.dict())
    db.add(db_alimento)
    db.commit()
    db.refresh(db_alimento)
    return db_alimento


def create_plate(db: Session, prato: schemas.PratoCreate):
    db_prato = models.Prato(**prato.dict())
    db.add(db_prato)
    db.commit()
    db.refresh(db_prato)
    return db_prato


def create_creation(db: Session, criacao: schemas.CriacaoCreate):
    db_criacao = models.Criacao(**criacao.dict())
    db.add(db_criacao)
    db.commit()
    db.refresh(db_criacao)
    return db_criacao


def delete_food(db: Session, alimento_id):
    alimento = get_food_by_id(db, alimento_id)
    if alimento:
        db.delete(alimento)
        db.commit()
        return True
    return  False


def delete_plate(db: Session, prato_id):
    prato = get_plate_by_id(db, prato_id)
    if prato:
        db.delete(prato)
        db.commit()
        return True
    return  False