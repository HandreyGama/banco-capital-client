
import customtkinter as ctk
from PIL import Image
from src.credencial_screen.server_handler.server_requests import *
ctk.set_appearance_mode("dark")

class TransferenciaApp:

    def __init__(self,controller):
        self.controller = controller
        self.app = ctk.CTk()
        self.app.geometry("1224x664")
        self.app.title("Dashboard - Banco CAPITAL")
        self.app.minsize(1224, 664)
        self.app.resizable(False, False)
        # Cores
        self.BLACK_BG = "#0a0a0a"
        self.DOURADO_BANCO_CAPITAL = "#C9A358"
        self.BRANCO_BG = "#D9D9D9"
        self.BRANCO_BG_CARD = "#E9E6E6"
        self.DOURADO_LIGTH = "#DBB96E"
        self.DOURADO_BLACK = "#B68C43"
        self.VERDE_LIGTH = "#74C88D"
        self.VERDE_BLACK = "#339651"
        self.VERMELHO_LIGTH = "#EE5F5F"
        self.VERMELHO_BLACK = "#BC1616"
        
        user = client_informacoes(self.controller.USER_INDEX)

        # Fonte com CTkFont
        self.AFACAD_BOLD = ctk.CTkFont(family="Afacad", size=24, weight="bold")
        self.AFACAD_REGULAR = ctk.CTkFont(family="Afacad", size=15, weight="normal")

        self.AFACAD_BOLD10 = ctk.CTkFont(family="Afacad", size=10, weight="bold")
        self.AFACAD_BOLD15 = ctk.CTkFont(family="Afacad", size=15, weight="bold")
        self.AFACAD_REGULAR20 = ctk.CTkFont(family="Afacad", size=20, weight="normal")

        # Frame principal
        frame = ctk.CTkFrame(master=self.app)
        frame.pack(fill="both", expand=True)

        def criar_botao(master, texto="", caminho_icon='', cor_fundo="transparent",command=None):

            imagem_icon = Image.open(caminho_icon).resize((24, 24))
            icon = ctk.CTkImage(light_image=imagem_icon, size=(24, 24))
            return ctk.CTkButton(
                master=master,
                image=icon,
                text=texto,
                compound="left",
                font=self.AFACAD_REGULAR,
                fg_color=cor_fundo,
                text_color="white" if cor_fundo == "transparent" else "white",
                hover_color="#1a1a1a" if cor_fundo == "transparent" else self.DOURADO_BLACK,
                anchor="w",
                width=120,
                height=40,
                corner_radius=6,
                command=command
            )
        
        btn_voltar = criar_botao(frame, texto="Voltar", caminho_icon='src/view/assets/icons/voltar.png',command=self.voltarParaDashboard)
        btn_voltar.place(x=20, y=20)
        

        user_info_frame = ctk.CTkFrame(master=frame, fg_color=self.BRANCO_BG, corner_radius=0)
        user_info_frame.pack(fill="both", expand=True)

        # Foto de perfil
        try:
            imagem_perfil = Image.open(user.get("foto_perfil", {}).get("avatar", {})).resize((40, 40))
        except:
            imagem_perfil = Image.open("src/view/assets/logotype/banco-capital.png").resize((40, 40))

        perfil_ctk_image = ctk.CTkImage(light_image=imagem_perfil, size=(40, 40))
        label_foto = ctk.CTkLabel(master=user_info_frame, image=perfil_ctk_image, text="", fg_color="transparent")
        # Saudação
        label_user = ctk.CTkLabel(
            master=user_info_frame,
            text=f"Olá",
            font=self.AFACAD_BOLD,
            text_color=self.BLACK_BG,
            fg_color="transparent"
        )
        label_user.pack(side="left", padx=(0, 10))  # texto primeiro, padding à direita
        label_foto.pack(side="left")               # imagem depois


    def voltarParaDashboard(self):
        self.app.destroy()
        self.controller.abrir_dashboard()

    def run(self):
        self.app.mainloop()