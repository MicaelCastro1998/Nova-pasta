import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import string
import random


# cadastro_funcionario.py
class CadastroFuncionario:
    def __init__(self, janela, usuarios, voltar_administrador_func):
        self.janela = janela
        self.usuarios = usuarios
        self.voltar_administrador_func = voltar_administrador_func  # Salva a função
        self.id_contador = len(usuarios)

        # Interface de cadastro
        for widget in self.janela.winfo_children():
            widget.destroy()

        label_nome = tk.Label(self.janela, text="Nome do Funcionário:")
        label_nome.grid(row=0, column=0, padx=10, pady=10)

        self.entry_nome = tk.Entry(self.janela)
        self.entry_nome.grid(row=0, column=1, padx=10, pady=10)

        label_cargo = tk.Label(self.janela, text="Cargo:")
        label_cargo.grid(row=1, column=0, padx=10, pady=10)

        # Combobox para selecionar o cargo
        self.cargos = ["Médico", "Recepcionista"]
        self.combo_cargo = ttk.Combobox(self.janela, values=self.cargos, state="readonly")
        self.combo_cargo.grid(row=1, column=1, padx=10, pady=10)
        self.combo_cargo.set("Selecione o Cargo")

        btn_cadastrar = tk.Button(self.janela, text="Cadastrar", command=self.cadastrar_funcionario)
        btn_cadastrar.grid(row=2, column=1, padx=10, pady=10)

        btn_voltar = tk.Button(self.janela, text="Voltar", command=self.voltar_administrador)
        btn_voltar.grid(row=3, column=1, padx=10, pady=10)

    def cadastrar_funcionario(self):
        nome = self.entry_nome.get()
        cargo = self.combo_cargo.get()

        if not nome or cargo not in self.cargos:
            messagebox.showerror("Erro", "Preencha corretamente os campos.")
            return

        self.id_contador += 1
        novo_id = f"{self.id_contador:06}"
        nova_senha = ''.join(random.choices(string.ascii_letters + string.digits, k=8))

        self.usuarios[novo_id] = {"senha": nova_senha, "cargo": cargo}
        messagebox.showinfo("Sucesso", f"Funcionário cadastrado!\nID: {novo_id}\nSenha: {nova_senha}")

    def voltar_administrador(self):
        self.voltar_administrador_func()  # Chama a função de voltar para a interface do administrador