from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from .database import Base


class Prato(Base):
    __tablename__ = "pratos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    tipo = Column(Integer)
    cor = Column(Integer)
    consistencia = Column(Integer)
    ingredientes = Column(String)



class Alimento(Base):
    __tablename__ = "alimentos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    valor = Column(Float)
    energia = Column(Float)
    proteinas = Column(Float)
    carboidratos = Column(Float)
    lipideos = Column(Float)
    fibras = Column(Float)
    calcio = Column(Float)
    ferro = Column(Float)
    zinco = Column(Float)
    magnesio = Column(Float)
  
 

