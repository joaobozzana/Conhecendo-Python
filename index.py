from tkinter import Tk, Label, Frame, ttk, Entry, PhotoImage
from tkinter import *
from tkinter import messagebox
from registro import Register
import DataBase

class IndexPage:

    def logar(self):
        Usuario = self.UsuarioEntry.get()
        Senha = self.SenhaEntry.get()

        DataBase.cursor.execute("""
            SELECT * FROM users 
            WHERE usuario = ? AND senha = ?
            """, (Usuario, Senha))
        print("Foi")
        VerificaLogin = DataBase.cursor.fetchone()
        try:
            if (Usuario in VerificaLogin and Senha in VerificaLogin):
                messagebox.showinfo(title="Informações de login", message="Acesso validado")
        except:
            messagebox.showerror(title="Informações de login", message="Acesso negado")

    def registrar(self):
        # Fechar a janela atual
        self.login.destroy()

        # Adicione os widgets e configurações necessários para a nova janela aqui
        register = Register()
        register.registro.mainloop()

    def __init__(self):
        self.login = Tk()
        self.login.title("Painel de login")
        self.login.geometry("600x300")
        self.login.configure(background="#E6E6E6")
        self.login.resizable(width=False, height=False)
        self.login.attributes("-alpha", 0.9)  # Transparência da janela

        # IMG
        self.logo = PhotoImage(file="icons/logo.png")

        # Widgets
        LeftFrame = Frame(self.login, width=200, height=300, bg="#BFBFBF", relief="solid", bd=2, borderwidth=1, padx=5, pady=5, highlightbackground="black", highlightcolor="black", highlightthickness=2)
        LeftFrame.pack(side=LEFT)

        RightFrame = Frame(self.login, width=400, height=300, bg="#BFBFBF", relief="solid", bd=2, borderwidth=1, padx=5, pady=5, highlightbackground="black", highlightcolor="black", highlightthickness=2)
        RightFrame.pack(side=RIGHT)

        # Logo
        largura_desejada = 100
        altura_desejada = 100
        self.logo = self.logo.subsample(int(self.logo.width() / largura_desejada), int(self.logo.height() / altura_desejada))

        LogoLabel = Label(LeftFrame, image=self.logo, bg="#BFBFBF")
        LogoLabel.place(x=40, y=80)

        # User
        UsuarioLabel = Label(RightFrame, text="Usuário:", font=("Century Gothic", 14), bg="#BFBFBF", fg="black")
        UsuarioLabel.place(x=5, y=70)

        self.UsuarioEntry = ttk.Entry(RightFrame, width=30)
        self.UsuarioEntry.place(x=115, y=75)
        self.UsuarioEntry.focus()  # Foca no campo de usuário inicialmente

        # Senha
        SenhaLabel = Label(RightFrame, text="Senha:", font=("Century Gothic", 14), bg="#BFBFBF", fg="black")
        SenhaLabel.place(x=5, y=120)

        self.SenhaEntry = ttk.Entry(RightFrame, width=30, show='●') 
        self.SenhaEntry.place(x=115, y=125)

        # Botoes
        button_bg = "#4CAF50"  # Cor de destaque para os botões

        LoginButton = ttk.Button(RightFrame, text="Login", width=30, style='TButton', command=self.logar)
        LoginButton.place(x=70, y=200)

        RegistroButton = ttk.Button(RightFrame, text="Registrar-se", width=30, style='TButton', command=self.registrar)
        RegistroButton.place(x=70, y=240)

        # Estilo para os botões
        style = ttk.Style()
        style.configure('TButton', font=('Century Gothic', 12), background=button_bg)

        self.login.mainloop()

    def run(self):
        self.login.mainloop()

if __name__ == "__main__":
    index_page = IndexPage()
    index_page.run()
