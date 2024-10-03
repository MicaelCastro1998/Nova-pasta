from tela_login import SistemaLogin
import tkinter as tk

def main():
    janela = tk.Tk()
    app = SistemaLogin(janela)
    janela.mainloop()

if __name__ == '__main__':
    main()