class PessoaView:
    @staticmethod
    def mostrar_pessoas(pessoas):
        for pessoa in pessoas:
            print(f"ID: {pessoa.id}, Nome: {pessoa.nome}, Idade: {pessoa.idade}, Altura: {pessoa.altura}, Profissão: {pessoa.profissao}")

    @staticmethod
    def mostrar_mensagem(mensagem):
        print(mensagem)