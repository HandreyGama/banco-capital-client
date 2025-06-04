import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import sys
import os
from src.credencial_screen.server_handler.server_requests import *

# Configuração inicial
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


class LoginApp:
    def __init__(self, controller):
        self.controller = controller
        self.app = ctk.CTk()
        self.app.geometry("600x400")
        self.app.title("Login - Banco CAPITAL")
        self.app.resizable(False, False)

        self.setup_ui()

    def setup_ui(self):

        # Cores personalizadas
        self.DARK_BG = "#121212"
        self.DARKER_BG = "#0a0a0a"
        self.DARK_FRAME = "#1e1e1e"
        self.ACCENT_COLOR = "#4a6fa5"
        self.ACCENT_HOVER = "#3a5a80"
        self.TEXT_COLOR = "#e0e0e0"
        self.SECONDARY_TEXT = "#a0a0a0"
        BORDA_PRETA = "#000000"

        frame = ctk.CTkFrame(master=self.app, fg_color=self.DARK_BG, corner_radius=20)
        frame.pack(pady=30, padx=30, fill="both", expand=True)

        left_frame = ctk.CTkFrame(
            master=frame, width=200, corner_radius=0, fg_color=self.DARK_BG
        )
        left_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)

        self.right_frame = ctk.CTkFrame(
            master=frame, fg_color=self.DARK_FRAME, corner_radius=20
        )
        self.right_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        try:
            qr_img = Image.open("src/view/assets/logotype/banco-capital.png")
            qr_img = qr_img.resize((150, 200))
            qr_img = ImageTk.PhotoImage(qr_img)
            qr_label = tk.Label(left_frame, image=qr_img, bg=self.DARK_BG)
            qr_label.image = qr_img
            qr_label.pack(pady=(40, 10))
        except:
            pass

        login_label = ctk.CTkLabel(
            self.right_frame,
            text="Login",
            font=("Arial", 24, "bold"),
            anchor="w",
            text_color=self.TEXT_COLOR,
        )
        login_label.pack(pady=(40, 20), padx=20)

        CAMPO_WIDTH = 250
        CAMPO_PADX = 20
        CAMPO_PADY = 10
        BORDA_WIDTH = 1

        self.cpf_entry = ctk.CTkEntry(
            self.right_frame,
            placeholder_text="CPF",
            width=CAMPO_WIDTH,
            fg_color=self.DARKER_BG,
            border_color=BORDA_PRETA,
            border_width=BORDA_WIDTH,
            text_color=self.TEXT_COLOR,
            corner_radius=5,
        )
        self.cpf_entry.pack(pady=CAMPO_PADY, padx=CAMPO_PADX)

        senha_container = ctk.CTkFrame(
            self.right_frame, fg_color="transparent", bg_color="transparent"
        )
        senha_container.pack(pady=CAMPO_PADY, padx=CAMPO_PADX)

        senha_border_frame = ctk.CTkFrame(
            senha_container,
            fg_color=self.DARKER_BG,
            border_color=BORDA_PRETA,
            border_width=BORDA_WIDTH,
            corner_radius=5,
        )
        senha_border_frame.pack()

        self.senha_entry = ctk.CTkEntry(
            senha_border_frame,
            placeholder_text="Senha",
            show="*",
            width=CAMPO_WIDTH - 30,
            fg_color=self.DARKER_BG,
            border_width=0,
            text_color=self.TEXT_COLOR,
        )
        self.senha_entry.pack(side="left", padx=0)

        toggle_btn = ctk.CTkButton(
            senha_border_frame,
            text="👁",
            width=30,
            height=28,
            fg_color=self.DARKER_BG,
            hover_color=self.DARK_FRAME,
            command=self.toggle_senha,
            corner_radius=0,
            border_width=0,
        )
        toggle_btn.pack(side="right", padx=0)

        login_button = ctk.CTkButton(
            self.right_frame,
            text="Login",
            width=CAMPO_WIDTH,
            fg_color="white",
            hover_color="gray",
            text_color="black",
            font=("Arial", 11, "bold"),
            corner_radius=5,
            command=self.verificar_login,
        )
        login_button.pack(padx=CAMPO_PADX)

        botoes_frame = ctk.CTkFrame(self.right_frame, fg_color=self.DARK_FRAME)
        botoes_frame.pack(pady=10)

        esquecisenha = ctk.CTkButton(
            botoes_frame,
            width=120,
            text="Esqueci minha senha",
            font=("Arial", 9),
            fg_color=self.DARK_FRAME,
            hover_color=self.DARKER_BG,
            text_color=self.SECONDARY_TEXT,
            border_width=0,
            command=self.abrir_forgout
        )
        esquecisenha.pack(side="left", padx=10)

        cadastrase = ctk.CTkButton(
            botoes_frame,
            width=100,
            text="Cadastre-se",
            font=("Arial", 9),
            fg_color=self.DARK_FRAME,
            hover_color=self.DARKER_BG,
            text_color=self.SECONDARY_TEXT,
            border_width=0,
            command=self.abrir_cadastro
        )
        cadastrase.pack(side="left", padx=10)

    def abrir_cadastro(self):
        return self.controller.abrir_cadastro()    
    def abrir_forgout(self):
        return self.controller.abrir_forgoutKey()      
    def toggle_senha(self):
        if self.senha_entry.cget("show") == "":
            self.senha_entry.configure(show="*")
        else:
            self.senha_entry.configure(show="")

    def verificar_login(self):
        cpf = self.cpf_entry.get()
        senha = self.senha_entry.get()

        if not cpf or not senha:
            messagebox.showwarning("Atenção", "Por favor, preencha todos os campos!")
            return
        self.controller.USER_EXISTS,self.controller.USER_INDEX = client_login(cpf,senha)

        if self.controller.USER_EXISTS:
            self.app.destroy()
            self.controller.abrir_dashboard()
        else:
            messagebox.showerror("Erro", "CPF ou senha incorretos!")

    def run(self):
        self.app.mainloop()
