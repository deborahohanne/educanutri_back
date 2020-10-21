from sqlalchemy.orm import Session
from api.model import models, schemas
from fastapi import FastAPI, APIRouter, Depends
from typing import List

from sqlalchemy.orm import Session
from api.model import crud, models, schemas, search
from api.model.database import SessionLocal



def generate_plate(refeicao: int, db: Session):

    list_pratos = []

    if refeicao == 1:
        arroz_acomp = search.search_plate(db=db, tipo=1)
        
        return arroz_acomp
