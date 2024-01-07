from tkinter import Tk, Label, Frame, ttk, Entry, PhotoImage
from tkinter import *
from tkinter import messagebox
from registro import Register
import DataBase

class IndexPage:

    # Função de validar o login
    def logar(self):
        Usuario = self.UsuarioEntry.get()
        Senha = self.SenhaEntry.get()

        DataBase.cursor.execute("""
            SELECT * FROM usuarios 
            WHERE usuario = ? AND senha = ?
            """, (Usuario, Senha))
        VerificaLogin = DataBase.cursor.fetchone()
        try:
            if (Usuario in VerificaLogin and Senha in VerificaLogin):
                messagebox.showinfo(title="Informações de login", message="Acesso validado")
        except:
            messagebox.showerror(title="Informações de login", message="Acesso negado")

    # Função pra chamar a janela de registro
    def registrar(self):
        self.login.destroy()
        register = Register()
        register.registro.mainloop()

    def __init__(self):
        self.login = Tk()
        self.login.title("Painel de login") # Nome

        # Obtém a resolução da tela
        largura_tela = self.login.winfo_screenwidth()
        altura_tela = self.login.winfo_screenheight()
        # Calcula a posição para centralizar a janela
        x_pos = (largura_tela - 600) // 2 
        y_pos = (altura_tela - 300) // 2  

        self.login.geometry(f"600x300+{x_pos}+{y_pos}")
        self.login.configure(background="#E6E6E6") # Cor
        self.login.resizable(width=False, height=False) # Proibe de aumentar/diminuir a janela
        self.login.attributes("-alpha", 0.9)  # Transparência da janela

        # IMG
        self.logo = PhotoImage(file="icons/logo.png")

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

        # Usuario
        UsuarioLabel = Label(RightFrame, text="Usuário:", font=("Century Gothic", 14), bg="#BFBFBF", fg="black")
        UsuarioLabel.place(x=5, y=70)
        self.UsuarioEntry = ttk.Entry(RightFrame, width=30)
        self.UsuarioEntry.place(x=115, y=75)
        self.UsuarioEntry.focus() 

        # Senha
        SenhaLabel = Label(RightFrame, text="Senha:", font=("Century Gothic", 14), bg="#BFBFBF", fg="black")
        SenhaLabel.place(x=5, y=120)
        self.SenhaEntry = ttk.Entry(RightFrame, width=30, show='●') 
        self.SenhaEntry.place(x=115, y=125)

        # Botoes
        button_bg = "#4CAF50"

        LoginButton = ttk.Button(RightFrame, text="Login", width=30, style='TButton', command=self.logar)
        LoginButton.place(x=70, y=200)

        RegistroButton = ttk.Button(RightFrame, text="Registrar-se", width=30, style='TButton', command=self.registrar)
        RegistroButton.place(x=70, y=240)

        style = ttk.Style()
        style.configure('TButton', font=('Century Gothic', 12), background=button_bg)

        self.login.mainloop()

    def run(self):
        self.login.mainloop()

if __name__ == "__main__":
    index_page = IndexPage()
    index_page.run()
