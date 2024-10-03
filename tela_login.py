import tkinter as tk
from tkinter import messagebox
from cadastro_funcionario import CadastroFuncionario


class SistemaLogin:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Sistema de Posto de Saúde")

        # Simulação de banco de dados de usuários (credenciais armazenadas como dicionário)
        self.usuarios = {
            "admin": {"senha": "admin123", "cargo": "Administrador"},
            "medico": {"senha": "medico123", "cargo": "Médico"},
            "recepcionista": {"senha": "recepcao123", "cargo": "Recepcionista"}
        }

        # Criar a interface de login
        self.criar_interface_login()

    def criar_interface_login(self):
        # Limpar a janela atual para trocar de interface
        for widget in self.janela.winfo_children():
            widget.destroy()

        # Interface de Login
        label_usuario = tk.Label(self.janela, text="Usuário:")
        label_usuario.grid(row=0, column=0, padx=10, pady=10)

        self.entry_usuario = tk.Entry(self.janela)
        self.entry_usuario.grid(row=0, column=1, padx=10, pady=10)

        label_senha = tk.Label(self.janela, text="Senha:")
        label_senha.grid(row=1, column=0, padx=10, pady=10)

        self.entry_senha = tk.Entry(self.janela, show="*")
        self.entry_senha.grid(row=1, column=1, padx=10, pady=10)

        btn_login = tk.Button(self.janela, text="Login", command=self.verificar_login)
        btn_login.grid(row=2, column=1, padx=10, pady=10)

    def verificar_login(self):
        usuario = self.entry_usuario.get()
        senha = self.entry_senha.get()

        if usuario in self.usuarios and self.usuarios[usuario]["senha"] == senha:
            cargo = self.usuarios[usuario]["cargo"]
            self.abrir_painel(cargo)
        else:
            messagebox.showerror("Erro", "Usuário ou senha incorretos")

    def abrir_painel(self, cargo):
        if cargo == "Administrador":
            messagebox.showinfo("Login bem-sucedido", "Bem-vindo, Administrador!")
            self.abrir_interface_administrador()
        elif cargo == "Médico":
            messagebox.showinfo("Login bem-sucedido", "Bem-vindo, Médico!")
        elif cargo == "Recepcionista":
            messagebox.showinfo("Login bem-sucedido", "Bem-vindo, Recepcionista!")
        else:
            messagebox.showerror("Erro", "Cargo não reconhecido")

    def abrir_interface_administrador(self):
        # Limpar a janela para a interface de administrador
        for widget in self.janela.winfo_children():
            widget.destroy()

        label_adm = tk.Label(self.janela, text="Administrador - Ações Disponíveis")
        label_adm.grid(row=0, column=0, padx=10, pady=10)

        btn_cadastrar_funcionario = tk.Button(self.janela, text="Cadastrar Funcionário", command=self.abrir_cadastro_funcionario)
        btn_cadastrar_funcionario.grid(row=1, column=0, padx=10, pady=10)

        btn_logout = tk.Button(self.janela, text="Logout", command=self.criar_interface_login)
        btn_logout.grid(row=2, column=0, padx=10, pady=10)
    
    def abrir_interface_administrador(self):
        # Limpar a janela para a interface de administrador
        for widget in self.janela.winfo_children():
            widget.destroy()

        label_adm = tk.Label(self.janela, text="Administrador - Ações Disponíveis")
        label_adm.grid(row=0, column=0, padx=10, pady=10)

        btn_cadastrar_funcionario = tk.Button(self.janela, text="Cadastrar Funcionário", command=self.abrir_cadastro_funcionario)
        btn_cadastrar_funcionario.grid(row=1, column=0, padx=10, pady=10)

        btn_logout = tk.Button(self.janela, text="Logout", command=self.criar_interface_login)
        btn_logout.grid(row=2, column=0, padx=10, pady=10)

    def abrir_cadastro_funcionario(self):
        CadastroFuncionario(self.janela, self.usuarios, self.abrir_interface_administrador)
    