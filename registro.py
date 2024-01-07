from distutils.util import execute
from tkinter import Tk, Label, messagebox, ttk, Entry, PhotoImage
import DataBase
import re

class Register:

    # Verificação da senha
    def criterios_da_senha(self, senha):
        # Pelo menos 6 caracteres
        if len(senha) < 6:
            return False
        # Pelo menos 1 letra maiúscula
        if not any(c.isupper() for c in senha):
            return False
        # Pelo menos 1 caracter especial
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', senha):
            return False
        # Pelo menos 1 número
        if not any(c.isdigit() for c in senha):
            return False
        return True

    # Função de voltar pra janela principal
    def back(self):
        self.registro.destroy()
        from index import IndexPage 
        index_page = IndexPage()
        index_page.run()

    # Função pra registrar novos usuarios e validar campos
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
        elif not self.criterios_da_senha(Senha):
            campos_vazios.append("Senha não atende aos critérios")

        if campos_vazios:
            mensagem = f"Preencha os seguintes campos: {', '.join(campos_vazios)}"
            messagebox.showerror(title="Registro invalidado", message=mensagem)
        else:
            DataBase.cursor.execute("""
                INSERT INTO usuarios(nome, email, usuario, senha) VALUES(?, ?, ?, ?)
            """, (Nome, Email, Usuario, Senha))

            DataBase.conn.commit()
            messagebox.showinfo(title="Informações de registro", message="Registro concluído")

    def exibir_mensagem_senha(self, event):
        self.CaixaMensagemSenha.config(text="A senha deve conter:\n- Letra maiúscula\n- Caracteres especiais\n- Números\n- Mínimo de 6 dígitos")

    def esconder_mensagem_senha(self, event):
        self.CaixaMensagemSenha.config(text="")

    def __init__(self):
        self.registro = Tk()
        self.registro.title("Painel de Registro")

        # Obtém a resolução da tela
        largura_tela = self.registro.winfo_screenwidth()
        altura_tela = self.registro.winfo_screenheight()

        # Calcula a posição para centralizar a janela
        x_pos = (largura_tela - 450) // 2  # Assumindo que a largura da janela é 400
        y_pos = (altura_tela - 400) // 2   # Assumindo que a altura da janela é 450

        self.registro.geometry(f"450x400+{x_pos}+{y_pos}")
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

        # Nome
        NomeLabel = Label(self.registro, text="Nome:", font=("Century Gothic", 14), bg="#E6E6E6")
        NomeLabel.place(x=15, y=70)
        self.NomeEntry = ttk.Entry(self.registro, width=30)
        self.NomeEntry.place(x=115, y=75)
        self.NomeEntry.focus()

        # Email
        EmailLabel = Label(self.registro, text="Email:", font=("Century Gothic", 14), bg="#E6E6E6")
        EmailLabel.place(x=15, y=120)
        self.EmailEntry = ttk.Entry(self.registro, width=30)
        self.EmailEntry.place(x=115, y=125)

        # Usuario
        UsuarioLabel = Label(self.registro, text="Usuário:", font=("Century Gothic", 14), bg="#E6E6E6")
        UsuarioLabel.place(x=15, y=170)
        self.UsuarioEntry = ttk.Entry(self.registro, width=30)
        self.UsuarioEntry.place(x=115, y=175)
        
        # Senha
        SenhaLabel = Label(self.registro, text="Senha:", font=("Century Gothic", 14), bg="#E6E6E6")
        SenhaLabel.place(x=15, y=220)
        self.SenhaEntry = ttk.Entry(self.registro, width=30, show='●') 
        self.SenhaEntry.place(x=115, y=225)

        # Caixa de mensagem para os critérios da senha
        self.CaixaMensagemSenha = ttk.Label(self.registro, text="", font=("Century Gothic", 8), background="#E6E6E6", foreground="red")
        self.CaixaMensagemSenha.place(x=315, y=235, anchor="w")

        # Vincula a função exibir_mensagem_senha ao evento Enter do Entry
        self.SenhaEntry.bind("<Enter>", self.exibir_mensagem_senha)
        # Vincula a função esconder_mensagem_senha ao evento Leave do Entry
        self.SenhaEntry.bind("<Leave>", self.esconder_mensagem_senha)

        # Botoes
        button_bg = "#4CAF50" 

        RegistroButton = ttk.Button(self.registro, text="Registrar", width=30, style='TButton', command=self.RegistertoDataBase)
        RegistroButton.place(x=70, y=280)

        VoltarButton = ttk.Button(self.registro, text="Voltar", width=30, style='TButton', command=self.back)
        VoltarButton.place(x=70, y=320)

        style = ttk.Style()
        style.configure('TButton', font=('Century Gothic', 12), background=button_bg)

        # Mantenha uma referência à imagem
        self.LogoLabel.image = logo

        self.registro.mainloop()

if __name__ == "__main__":
    registro = Register()
