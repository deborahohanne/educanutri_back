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
    
    criacao = relationship("Criacao", back_populates="pratos")


class Alimento(Base):
    __tablename__ = "alimentos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    valor = Column(Float)
    energia = Column(Integer)
    proteinas = Column(Float)
    carboidratos = Column(Float)
    lipideos = Column(Float)
    fibras = Column(Float)
    calcio = Column(Integer)
    ferro = Column(Float)
    zinco = Column(Float)
    magnesio = Column(Integer)
    grupo = Column(Integer)

    criacao = relationship("Criacao", back_populates="alimentos")
  
class Criacao(Base):
    __tablename__ = "criacao"

    id = Column(Integer, primary_key=True, index=True)
    id_alimento = Column(Integer, ForeignKey("alimentos.id"))
    id_prato = Column(Integer, ForeignKey("pratos.id"))

    pratos = relationship("Prato", back_populates="criacao")
    alimentos = relationship("Alimento", back_populates="criacao")