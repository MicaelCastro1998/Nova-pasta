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
    email = Column(String, nullable=False)

DATABASE_URL = "postgresql+psycopg2://postgres:postgres@localhost/senac"
engine = create_engine(DATABASE_URL)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def listar_pessoas():
    pessoas = session.query(Pessoa).all()
    for pessoa in pessoas:
        print(f"ID: {pessoa.id}, Nome: {pessoa.nome}, Idade: {pessoa.idade}, Altura: {pessoa.altura}, Profissão: {pessoa.profissao}, E-mail: {pessoa.email}")

def cadastrar_pessoa(nome, idade, altura, profissao, email):
    nova_pessoa = Pessoa(nome=nome, idade=idade, altura=altura, profissao=profissao, email=email)
    session.add(nova_pessoa)
    session.commit()
    print(f"Pessoa '{nome}' cadastrada com sucesso!")

def editar_pessoa(id_pessoa, nome=None, idade=None, altura=None, profissao=None, email=None):
    pessoa = session.query(Pessoa).filter_by(id=id_pessoa).first()
    if pessoa:
        if nome:
            pessoa.nome = nome
        if idade:
            pessoa.idade = idade
        if altura:
            pessoa.altura = altura
        if profissao:
            pessoa.profissao = profissao
        if email:
            pessoa.email = email
        session.commit()
        print(f"Pessoa com ID {id_pessoa} atualizada com sucesso!")
    else:
        print(f"Pessoa com ID {id_pessoa} não encontrada.")

def excluir_pessoa(id_pessoa):
    pessoa = session.query(Pessoa).filter_by(id=id_pessoa).first()
    if pessoa:
        session.delete(pessoa)
        session.commit()
        print(f"Pessoa com ID {id_pessoa} excluída com sucesso!")
    else:
        print(f"Pessoa com ID {id_pessoa} não encontrada.")

cadastrar_pessoa("João", 30, 1.75, "Engenheiro")
cadastrar_pessoa("Maria", 25, 1.68, "Arquiteta")
cadastrar_pessoa("Carlos", 40, 1.80, "Médico")
cadastrar_pessoa("Ana", 35, 1.65, "Professora")
cadastrar_pessoa("Pedro", 28, 1.78, "Designer")

listar_pessoas()

editar_pessoa(3, nome="Carlos da Silva", idade=41)

excluir_pessoa(1)

listar_pessoas()