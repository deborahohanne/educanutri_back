from typing import List, Optional

from pydantic import BaseModel


class AlimentoBase(BaseModel):
    nome: str
    valor: float
    energia: int
    proteinas: float
    carboidratos: float
    lipideos: float
    fibras: float
    calcio: int
    ferro: float
    zinco: float
    magnesio: int


class AlimentoCreate(AlimentoBase):
    pass


class Alimento(BaseModel):
    id: int
    nome: str

    class Config:
        orm_mode = True


class PratoBase(BaseModel):
    nome: str
    tipo: int
    cor: int
    consistencia: int
    ingredientes: List[Alimento] = []


class PratoCreate(PratoBase):
    pass


class Prato(BaseModel):
    id: int
    alimentos: List[Alimento] = []

    class Config:
        orm_mode = True