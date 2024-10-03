from model.pessoa_model import Pessoa, get_session

class PessoaController:
    def __init__(self):
        self.session = get_session()

    def listar_pessoas(self):
        pessoas = self.session.query(Pessoa).all()
        return pessoas

    def cadastrar_pessoa(self, nome, idade, altura, profissao):
        nova_pessoa = Pessoa(nome=nome, idade=idade, altura=altura, profissao=profissao)
        self.session.add(nova_pessoa)
        self.session.commit()
        return f"Pessoa '{nome}' cadastrada com sucesso!"

    def editar_pessoa(self, id_pessoa, nome=None, idade=None, altura=None, profissao=None):
        pessoa = self.session.query(Pessoa).filter_by(id=id_pessoa).first()
        if pessoa:
            if nome:
                pessoa.nome = nome
            if idade:
                pessoa.idade = idade
            if altura:
                pessoa.altura = altura
            if profissao:
                pessoa.profissao = profissao
            self.session.commit()
            return f"Pessoa com ID {id_pessoa} atualizada com sucesso!"
        else:
            return f"Pessoa com ID {id_pessoa} não encontrada."

    def excluir_pessoa(self, id_pessoa):
        pessoa = self.session.query(Pessoa).filter_by(id=id_pessoa).first()
        if pessoa:
            self.session.delete(pessoa)
            self.session.commit()
            return f"Pessoa com ID {id_pessoa} excluída com sucesso!"
        else:
            return f"Pessoa com ID {id_pessoa} não encontrada."