import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Configuração inicial
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class LoginApp:
    def __init__(self):
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

        frame = ctk.CTkFrame(
            master=self.app,
            fg_color=self.DARK_BG,
            corner_radius=20
        )
        frame.pack(pady=30, padx=30, fill="both", expand=True)

        left_frame = ctk.CTkFrame(
            master=frame,
            width=200,
            corner_radius=0,
            fg_color=self.DARK_BG
        )
        left_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)

        self.right_frame = ctk.CTkFrame(
            master=frame,
            fg_color=self.DARK_FRAME,
            corner_radius=20
        )
        self.right_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        try:
            qr_img = Image.open("banco-capital.png")
            qr_img = qr_img.resize((150, 200))
            qr_img = ImageTk.PhotoImage(qr_img)
            qr_label = tk.Label(
                left_frame,
                image=qr_img,
                bg=self.DARK_BG
            )
            qr_label.image = qr_img
            qr_label.pack(pady=(40, 10))
        except:
            pass

        login_label = ctk.CTkLabel(
            self.right_frame,
            text="Login",
            font=("Arial", 24, "bold"),
            anchor="w",
            text_color=self.TEXT_COLOR
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
            corner_radius=5
        )
        self.cpf_entry.pack(pady=CAMPO_PADY, padx=CAMPO_PADX)

        senha_container = ctk.CTkFrame(
            self.right_frame,
            fg_color="transparent",
            bg_color="transparent"
        )
        senha_container.pack(pady=CAMPO_PADY, padx=CAMPO_PADX)

        senha_border_frame = ctk.CTkFrame(
            senha_container,
            fg_color=self.DARKER_BG,
            border_color=BORDA_PRETA,
            border_width=BORDA_WIDTH,
            corner_radius=5
        )
        senha_border_frame.pack()

        self.senha_entry = ctk.CTkEntry(
            senha_border_frame,
            placeholder_text="Senha",
            show="*",
            width=CAMPO_WIDTH-30,
            fg_color=self.DARKER_BG,
            border_width=0,
            text_color=self.TEXT_COLOR
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
            border_width=0
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
            command=self.verificar_login
        )
        login_button.pack(padx=CAMPO_PADX)

        botoes_frame = ctk.CTkFrame(
            self.right_frame,
            fg_color=self.DARK_FRAME
        )
        botoes_frame.pack(pady=10)

        esquecisenha = ctk.CTkButton(
            botoes_frame,
            width=120,
            text="Esqueci minha senha",
            font=("Arial", 9),
            fg_color=self.DARK_FRAME,
            hover_color=self.DARKER_BG,
            text_color=self.SECONDARY_TEXT,
            border_width=0
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
            border_width=0
        )
        cadastrase.pack(side="left", padx=10)

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

        if cpf == "123.456.789-00" and senha == "senha123":
            self.abrir_tela_inicio()
        else:
            messagebox.showerror("Erro", "CPF ou senha incorretos!")

    def abrir_tela_inicio(self):
        self.app.destroy()

        inicio_app = ctk.CTk()
        inicio_app.geometry("1000x600")
        inicio_app.title("Banco CAPITAL - Dashboard")

        sidebar = ctk.CTkFrame(inicio_app, width=80, fg_color=self.DARKER_BG, corner_radius=0)
        sidebar.pack(side="left", fill="y")

        for icon in ["🏠", "💳", "📈", "💬", "⚙️"]:
            ctk.CTkButton(sidebar, text=icon, fg_color="transparent", text_color=self.TEXT_COLOR, hover_color=self.DARK_FRAME).pack(pady=15)

        main_frame = ctk.CTkFrame(inicio_app, fg_color=self.DARK_BG)
        main_frame.pack(side="left", fill="both", expand=True)

        header = ctk.CTkFrame(main_frame, height=60, fg_color=self.DARK_FRAME)
        header.pack(fill="x")

        ctk.CTkLabel(header, text="Dashboard", font=("Arial", 20, "bold"), text_color=self.TEXT_COLOR).pack(side="left", padx=20)

        cards_frame = ctk.CTkFrame(main_frame, fg_color=self.DARK_BG)
        cards_frame.pack(pady=10, padx=20, fill="x")

        valores = [
            ("💳", "Shopping, Débito e Crédito", "R$ 597"),
            ("🔁", "Transferência Internacional", "R$ 875"),
            ("🛡️", "Investimento & Seguros", "R$ 1380"),
            ("🎓", "Educação & Hobbies", "R$ 1200"),
        ]

        for icon, desc, valor in valores:
            card = ctk.CTkFrame(cards_frame, width=200, height=100, corner_radius=12, fg_color=self.DARK_FRAME)
            card.pack(side="left", padx=10, pady=10)
            ctk.CTkLabel(card, text=icon, font=("Arial", 24), text_color=self.ACCENT_COLOR).pack()
            ctk.CTkLabel(card, text=valor, font=("Arial", 16, "bold"), text_color=self.TEXT_COLOR).pack()
            ctk.CTkLabel(card, text=desc, font=("Arial", 10), text_color=self.SECONDARY_TEXT).pack()

        historico_frame = ctk.CTkFrame(main_frame, fg_color=self.DARK_FRAME)
        historico_frame.pack(pady=20, padx=20, fill="x")

        ctk.CTkLabel(historico_frame, text="Histórico de Transações", font=("Arial", 14, "bold"), text_color=self.TEXT_COLOR).pack(anchor="w", padx=10, pady=10)

        transacoes = [
            ("James Smith", "Graphic Design", "29/06/22", "R$ 259.50", "✅"),
            ("Robert William", "Photo Editing", "25/06/22", "R$ 490.00", "❗"),
            ("Linda Brown", "Financial Planner", "21/06/22", "R$ 374.00", "✅"),
            ("Michael Brown", "Architect Services", "17/06/22", "R$ 842.00", "✅")
        ]

        for nome, servico, data, valor, status in transacoes:
            linha = f"{nome} | {servico} | {data} | {valor} {status}"
            ctk.CTkLabel(historico_frame, text=linha, font=("Arial", 12), text_color=self.TEXT_COLOR).pack(anchor="w", padx=10)

        inicio_app.mainloop()

    def run(self):
        self.app.mainloop()

# Iniciar aplicação
if __name__ == "__main__":
    app = LoginApp()
    app.run()
