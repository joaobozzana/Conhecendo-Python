from tkinter import Tk, Label, Frame, ttk, Entry, PhotoImage
from tkinter import *
from tkinter import messagebox
from registro import Register

class IndexPage:
    def sua_funcao(self):
        # Fechar a janela atual
        self.login.destroy()

        # Adicione os widgets e configurações necessários para a nova janela aqui
        register = Register()
        register.registro.mainloop()

    def __init__(self):
        self.login = Tk()
        self.login.title("Acesso do Painel")
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
        UserLabel = Label(RightFrame, text="Username:", font=("Century Gothic", 14), bg="#BFBFBF", fg="black")
        UserLabel.place(x=5, y=70)

        UserEntry = ttk.Entry(RightFrame, width=30)
        UserEntry.place(x=115, y=75)
        UserEntry.focus()  # Foca no campo de usuário inicialmente

        # Senha
        PassLabel = Label(RightFrame, text="Password:", font=("Century Gothic", 14), bg="#BFBFBF", fg="black")
        PassLabel.place(x=5, y=120)

        PassEntry = ttk.Entry(RightFrame, width=30, show='●') 
        PassEntry.place(x=115, y=125)

        # Botoes
        button_bg = "#4CAF50"  # Cor de destaque para os botões

        LoginButton = ttk.Button(RightFrame, text="Login", width=30, style='TButton')
        LoginButton.place(x=70, y=200)

        RegisterButton = ttk.Button(RightFrame, text="Register", width=30, style='TButton', command=self.sua_funcao)
        RegisterButton.place(x=70, y=240)

        # Estilo para os botões
        style = ttk.Style()
        style.configure('TButton', font=('Century Gothic', 12), background=button_bg)

        self.login.mainloop()

    def run(self):
        self.login.mainloop()

if __name__ == "__main__":
    index_page = IndexPage()
    index_page.run()
