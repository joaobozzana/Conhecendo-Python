from distutils.util import execute
from tkinter import Tk, Label, messagebox, ttk, Entry, PhotoImage
from turtle import back
import DataBase

class Register:

    def back(self):
        # Fechar a janela atual
        self.registro.destroy()

        from index import IndexPage  # Importa a classe IndexPage do arquivo index.py
        index_page = IndexPage()
        index_page.run()

    def RegistertoDataBase(self):
        Nome = self.NomeEntry.get()
        Email = self.EmailEntry.get()
        Usuario = self.UsuarioEntry.get()
        Senha = self.SenhaEntry.get()

        campos_vazios = []
        if Nome == "":
            campos_vazios.append("Nome")
        if Email == "":
            campos_vazios.append("Email")
        if Usuario == "":
            campos_vazios.append("Usuário")
        if Senha == "":
            campos_vazios.append("Senha")

        if campos_vazios:
            mensagem = f"Preencha os seguintes campos: {', '.join(campos_vazios)}"
            messagebox.showerror(title="Registro invalidado", message=mensagem)
        else:
            DataBase.cursor.execute("""
                INSERT INTO users(nome, email, usuario, senha) VALUES(?, ?, ?, ?)
            """, (Nome, Email, Usuario, Senha))

            DataBase.conn.commit()
            messagebox.showinfo(title="Informações de registro", message="Registro concluído")

    def __init__(self):
        self.registro = Tk()
        self.registro.title("Painel de Registro")
        self.registro.geometry("400x400")
        self.registro.configure(background="#E6E6E6")
        self.registro.resizable(width=False, height=False)
        self.registro.attributes("-alpha", 0.9)  # Transparência da janela

        # LOGO
        logo = PhotoImage(file="icons/logo.png")
        largura_desejada = 50
        altura_desejada = 50
        logo = logo.subsample(int(logo.width() / largura_desejada), int(logo.height() / altura_desejada))

        self.LogoLabel = Label(self.registro, image=logo, bg="#E6E6E6")
        self.LogoLabel.place(x=180, y=10)

        # Configurações adicionais, widgets, etc.

        NomeLabel = Label(self.registro, text="Nome:", font=("Century Gothic", 14), bg="#E6E6E6")
        NomeLabel.place(x=15, y=70)
        self.NomeEntry = ttk.Entry(self.registro, width=30)
        self.NomeEntry.place(x=115, y=75)
        self.NomeEntry.focus()

        EmailLabel = Label(self.registro, text="Email:", font=("Century Gothic", 14), bg="#E6E6E6")
        EmailLabel.place(x=15, y=120)
        self.EmailEntry = ttk.Entry(self.registro, width=30)
        self.EmailEntry.place(x=115, y=125)

        UsuarioLabel = Label(self.registro, text="Usuário:", font=("Century Gothic", 14), bg="#E6E6E6")
        UsuarioLabel.place(x=15, y=170)
        self.UsuarioEntry = ttk.Entry(self.registro, width=30)
        self.UsuarioEntry.place(x=115, y=175)
        
        SenhaLabel = Label(self.registro, text="Senha:", font=("Century Gothic", 14), bg="#E6E6E6")
        SenhaLabel.place(x=15, y=220)
        self.SenhaEntry = ttk.Entry(self.registro, width=30, show='●') 
        self.SenhaEntry.place(x=115, y=225)

        # Botoes
        button_bg = "#4CAF50"  # Cor de destaque para os botões

        RegistroButton = ttk.Button(self.registro, text="Registrar", width=30, style='TButton', command=self.RegistertoDataBase)
        RegistroButton.place(x=70, y=280)

        VoltarButton = ttk.Button(self.registro, text="Voltar", width=30, style='TButton', command=self.back)
        VoltarButton.place(x=70, y=320)

        # Estilo para os botões
        style = ttk.Style()
        style.configure('TButton', font=('Century Gothic', 12), background=button_bg)

        # Mantenha uma referência à imagem
        self.LogoLabel.image = logo

        self.registro.mainloop()

if __name__ == "__main__":
    registro = Register()
