from controller.pessoa_controller import PessoaController
from view.pessoa_view import PessoaView

def main():
    controller = PessoaController()
    view = PessoaView()

    # Cadastrando algumas pessoas
    view.mostrar_mensagem(controller.cadastrar_pessoa("João", 30, 1.75, "Engenheiro"))
    view.mostrar_mensagem(controller.cadastrar_pessoa("Maria", 25, 1.68, "Arquiteta"))
    view.mostrar_mensagem(controller.cadastrar_pessoa("Carlos", 40, 1.80, "Médico"))
    view.mostrar_mensagem(controller.cadastrar_pessoa("Ana", 35, 1.65, "Professora"))
    view.mostrar_mensagem(controller.cadastrar_pessoa("Pedro", 28, 1.78, "Designer"))

    # Listando pessoas
    pessoas = controller.listar_pessoas()
    view.mostrar_pessoas(pessoas)

    # Editando uma pessoa
    view.mostrar_mensagem(controller.editar_pessoa(3, nome="Carlos da Silva", idade=41))

    # Excluindo uma pessoa
    view.mostrar_mensagem(controller.excluir_pessoa(5))

    # Listando pessoas novamente
    pessoas = controller.listar_pessoas()
    view.mostrar_pessoas(pessoas)

if __name__ == "__main__":
    main()