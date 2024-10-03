from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Pessoa(Base):
    __tablename__ = 'pessoa'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    idade = Column(Integer, nullable=False)
    altura = Column(Float, nullable=False)
    profissao = Column(String, nullable=False)

DATABASE_URL = "postgresql+psycopg2://usuario:senha@localhost/senac"
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

def get_session():
    return Session()
