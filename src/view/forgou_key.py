import customtkinter as ctk
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from tkinter import messagebox
from src.credencial_screen.server_handler.server_requests import *
from src.credencial_screen.credencial_shell import *
# Configurações do e-mail remetente
EMAIL_REMETENTE = "vm7451@gmail.com"
SENHA_REMETENTE = "vm20213293881723Alagoas__Email"

class EsqueciSenhaApp(ctk.CTkToplevel):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Recuperar Senha")
        self.geometry("400x300")
        self.resizable(False, False)
        self.configure(fg_color="#f9f9f9")
        self.user = client_informacoes(self.controller.USER_INDEX)
                                   
        ctk.CTkLabel(self, text="Esqueceu sua senha?", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=20)
        ctk.CTkLabel(self, text="Digite seu e-mail para receber instruções.").pack(pady=5)

        self.email_entry = ctk.CTkEntry(self, placeholder_text="Seu e-mail", width=300)
        self.email_entry.pack(pady=10)

        ctk.CTkButton(self, text="Enviar E-mail", command=self.enviar_email).pack(pady=15)

    def enviar_email(self):
        destinatario = self.email_entry.get()

        if not validar_email(destinatario):
            messagebox.showerror("Erro", "Digite um e-mail válido.")
            return

        try:
            mensagem = MIMEMultipart()
            mensagem["From"] = EMAIL_REMETENTE
            mensagem["To"] = destinatario
            mensagem["Subject"] = "Recuperação de Senha - Banco Capital"
            corpo = f"Olá,\n\nClique no link abaixo para redefinir sua senha:\n{self.user['senha']}"
            mensagem.attach(MIMEText(corpo, "plain"))

            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()
                server.login(EMAIL_REMETENTE, SENHA_REMETENTE)
                server.send_message(mensagem)

            messagebox.showinfo("Sucesso", "E-mail enviado com sucesso!")
        except Exception as e:
            print(f"Erro ao enviar e-mail: {e}")
            messagebox.showerror("Erro", "Ocorreu um erro ao enviar o e-mail.")

    def run(self):
        self.mainloop()  # Opcional: pode ser chamado no controller se preferir