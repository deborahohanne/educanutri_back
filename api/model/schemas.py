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
    grupo: int


class AlimentoCreate(AlimentoBase):
    pass


class Alimento(BaseModel):
    id: int

    class Config:
        orm_mode = True


class PratoBase(BaseModel):
    nome: str
    tipo: int
    cor: int
    consistencia: int


class PratoCreate(PratoBase):
    pass


class Prato(BaseModel):
    id: int

    class Config:
        orm_mode = True


class CriacaoBase(BaseModel):
    id_alimento: int
    id_prato: int


class CriacaoCreate(CriacaoBase):
    pass


class Criacao(BaseModel):
    id: int
    id_alimento: int
    id_prato: int

    class Config:
        orm_mode = True