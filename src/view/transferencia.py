import customtkinter as ctk
from PIL import Image
from src.credencial_screen.server_handler.server_requests import *

ctk.set_appearance_mode("dark")


class TransferenciaApp:
    def __init__(self, controller):
        self.controller = controller
        self.app = ctk.CTk()
        self.app.geometry("1224x664")
        self.app.title("Dashboard - Banco CAPITAL")
        self.app.resizable(False, False)
        self.num_conta = 0
        self.valor_transferencia = 0
        # Paleta de cores
        self.BLACK_BG = "#0a0a0a"
        self.DOURADO = "#C9A358"
        self.VERDE_LIGTH = "#74C88D"
        self.VERMELHO = "#FF4C4C"
        self.BRANCO = "#F0F0F0"
        self.saldo_client = 0
        # Fontes
        self.AFACAD_BOLD = ctk.CTkFont(family="Afacad", size=20, weight="bold")
        self.AFACAD_REGULAR = ctk.CTkFont(family="Afacad", size=14)

        self.user = client_informacoes(self.controller.USER_INDEX)
        self.destinatario = None

        self.main_frame = ctk.CTkFrame(self.app, fg_color=self.BLACK_BG)
        self.main_frame.pack(fill="both", expand=True)

        self.build_interface()

    def build_interface(self):
        # Botão voltar
        voltar = ctk.CTkButton(
            self.main_frame,
            text="← Voltar",
            command=self.voltar,
            fg_color="transparent",
            text_color=self.DOURADO,
            font=self.AFACAD_BOLD,
            hover_color="#1a1a1a",
        )
        voltar.place(x=20, y=20)

        # Área de transferência
        self.area = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.area.place(relx=0.5, rely=0.5, anchor="center")

        # Lado do remetente
        self.remetente_frame = ctk.CTkFrame(
            self.area, width=500, height=400, corner_radius=15, fg_color="#1f1f1f"
        )
        self.remetente_frame.pack(side="left", padx=30, pady=20)
        self.remetente_frame.pack_propagate(False)
        self.carregar_usuario(self.remetente_frame, self.user, "Você")

        # Lado do destinatário
        self.destinatario_frame = ctk.CTkFrame(
            self.area, width=500, height=400, corner_radius=15, fg_color="#1f1f1f"
        )
        self.destinatario_frame.pack(side="right", padx=30, pady=20)
        self.destinatario_frame.pack_propagate(False)
        self.input_conta = ctk.CTkEntry(
            self.destinatario_frame, placeholder_text="Número da conta", width=250
        )
        self.input_conta.pack(pady=20)
        self.btn_verificar = ctk.CTkButton(
            self.destinatario_frame, text="Verificar", command=self.verificar_conta
        )
        self.btn_verificar.pack()

    def carregar_usuario(self, frame, dados, titulo):
        ctk.CTkLabel(
            frame, text=titulo, font=self.AFACAD_BOLD, text_color=self.DOURADO
        ).pack(pady=10)

        try:
            imagem = Image.open(dados["foto_perfil"]["avatar"]).resize((60, 60))
        except:
            imagem = Image.open("src/view/assets/logotype/banco-capital.png").resize(
                (60, 60)
            )

        foto = ctk.CTkImage(imagem)
        ctk.CTkLabel(frame, image=foto, text="").pack()
        ctk.CTkLabel(
            frame,
            text=f"Nome: {dados['nome']}",
            font=self.AFACAD_REGULAR,
            text_color="white",
        ).pack(pady=4)
        if titulo == "Você":
            ctk.CTkLabel(
                frame,
                text=f"Saldo: R${float(dados['saldo']):.2f}",
                font=self.AFACAD_REGULAR,
                text_color=self.VERDE_LIGTH,
            ).pack(pady=4)
        self.saldo_client = float(dados["saldo"])

    def verificar_conta(self):
        num_conta = self.input_conta.get()
        self.destinatario = client_get_user_target(num_conta)
        self.num_conta = num_conta
        for widget in self.destinatario_frame.winfo_children():
            widget.destroy()

        if self.destinatario:
            self.carregar_usuario(
                self.destinatario_frame, self.destinatario, "Destinatário"
            )
            self.input_valor = ctk.CTkEntry(
                self.destinatario_frame, placeholder_text="Valor", width=200
            )
            self.input_valor.pack(pady=10)
            self.btn_transferir = ctk.CTkButton(
                self.destinatario_frame,
                text="Transferir",
                fg_color=self.DOURADO,
                command=self.realizar_transferencia,
            )
            self.btn_transferir.pack(pady=10)
        else:
            ctk.CTkLabel(
                self.destinatario_frame,
                text="Usuário não encontrado.",
                text_color=self.VERMELHO,
                font=self.AFACAD_BOLD,
            ).pack(pady=20)
        if self.input_valor and self.input_valor.winfo_exists():
            self.valor_transferencia = self.input_valor.get()
        else:
            print("valor não encontrado!")

    def realizar_transferencia(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        client_tranferencia(
            self.controller.USER_INDEX,
            self.valor_transferencia,
            self.num_conta,
            self.saldo_client,
        )
        sucesso = ctk.CTkLabel(
            self.main_frame,
            text="✅ Transferência realizada com sucesso!",
            font=self.AFACAD_BOLD,
            text_color=self.VERDE_LIGTH,
        )
        sucesso.place(relx=0.5, rely=0.4, anchor="center")

        novo = ctk.CTkButton(
            self.main_frame,
            text="Nova transferência",
            command=self.reiniciar,
            fg_color=self.DOURADO,
        )
        novo.place(relx=0.5, rely=0.5, anchor="center")

    def reiniciar(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        self.build_interface()

    def voltar(self):
        self.app.destroy()
        self.controller.abrir_dashboard()

    def run(self):
        self.app.mainloop()
