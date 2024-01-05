from distutils.util import execute
from tkinter import Tk, Label, messagebox, ttk, Entry, PhotoImage
from turtle import back
import DataBase


class Register:

    def back(self):
        # Implemente o código da sua função aqui
        print("Botão de back clicado!")

        # Fechar a janela atual
        self.registro.destroy()

        from index import IndexPage  # Importa a classe IndexPage do arquivo index.py
        index_page = IndexPage()
        index_page.run()

    def RegistertoDataBase(self):
        Name = self.NameEntry.get()
        Email = self.EmailEntry.get()
        User = self.UserEntry.get()
        Pass = self.PassEntry.get()
        DataBase.cursor.execute("""
            INSERT INTO users(Name, Email, User, Password) VALUES(?, ?, ?, ?)
        """, (Name, Email, User, Pass))

        DataBase.conn.commit()
        messagebox.showinfo(title="Register Info", message="Registration completed")

    def __init__(self):
        self.registro = Tk()
        self.registro.title("Acesso do Painel")
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

        NameLabel = Label(self.registro, text="Name:", font=("Century Gothic", 14), bg="#E6E6E6")
        NameLabel.place(x=15, y=70)
        self.NameEntry = ttk.Entry(self.registro, width=30)
        self.NameEntry.place(x=115, y=75)
        self.NameEntry.focus()

        EmailLabel = Label(self.registro, text="Email:", font=("Century Gothic", 14), bg="#E6E6E6")
        EmailLabel.place(x=15, y=120)
        self.EmailEntry = ttk.Entry(self.registro, width=30)
        self.EmailEntry.place(x=115, y=125)

        UserLabel = Label(self.registro, text="Username:", font=("Century Gothic", 14), bg="#E6E6E6")
        UserLabel.place(x=15, y=170)
        self.UserEntry = ttk.Entry(self.registro, width=30)
        self.UserEntry.place(x=115, y=175)
        
        PassLabel = Label(self.registro, text="Password:", font=("Century Gothic", 14), bg="#E6E6E6")
        PassLabel.place(x=15, y=220)
        self.PassEntry = ttk.Entry(self.registro, width=30, show='●') 
        self.PassEntry.place(x=115, y=225)

        # Botoes
        button_bg = "#4CAF50"  # Cor de destaque para os botões

        RegisterButton = ttk.Button(self.registro, text="Register", width=30, style='TButton', command=self.RegistertoDataBase)
        RegisterButton.place(x=70, y=280)

        BackButton = ttk.Button(self.registro, text="Back", width=30, style='TButton', command=self.back)
        BackButton.place(x=70, y=320)

        # Estilo para os botões
        style = ttk.Style()
        style.configure('TButton', font=('Century Gothic', 12), background=button_bg)

        # Mantenha uma referência à imagem
        self.LogoLabel.image = logo

        self.registro.mainloop()

if __name__ == "__main__":
    registro = Register()
