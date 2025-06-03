
import customtkinter as ctk
from PIL import Image
from src.credencial_screen.server_handler.server_requests import *

ctk.set_appearance_mode("dark")

class DashboardApp:

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

        frame2 = ctk.CTkFrame(master=frame, fg_color=self.BRANCO_BG, corner_radius=0)
        frame2.pack(fill="both", expand=True)

        # Sidebar
        sidebar = ctk.CTkFrame(master=frame2, fg_color=self.BLACK_BG, width=141, height=1224, corner_radius=0)
        sidebar.pack(side="left", fill="y")
        sidebar.pack_propagate(False)

        # Logo container
        logo_container = ctk.CTkFrame(master=sidebar, fg_color="transparent", width=141, height=100)
        logo_container.pack(pady=10)
        logo_container.pack_propagate(False)

        # Logo
        original_logo = Image.open("src/view/assets/logotype/banco-capital.png")
        resized_logo = original_logo.resize((62, 93))
        self.logo_image = ctk.CTkImage(light_image=resized_logo, size=(62, 93))
        logo_label = ctk.CTkLabel(master=logo_container, image=self.logo_image, text="", fg_color="transparent")
        logo_label.place(relx=0.5, rely=0.5, anchor="center")

        # Função auxiliar para criar botões com ícones
        def criar_botao_sidebar(master, texto, caminho_icon, cor_fundo="transparent"):

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
                corner_radius=6
            )

        # Container central para os botões
        middle_container = ctk.CTkFrame(master=sidebar, fg_color="transparent")
        middle_container.pack(expand=True)

        # Botões do meio
        btn_transferir = criar_botao_sidebar(middle_container, "Transferir", "src/view/assets/icons/transferir.png")
        btn_investir = criar_botao_sidebar(middle_container, "Investir", "src/view/assets/icons/investir.png")
        btn_extrato = criar_botao_sidebar(middle_container, "Extrato", "src/view/assets/icons/extrato.png")

        btn_transferir.pack(pady=(10, 0), padx=10, anchor="w")
        btn_investir.pack(pady=(10, 0), padx=10, anchor="w")
        btn_extrato.pack(pady=(10, 20), padx=10, anchor="w")

        # Container para os botões "Conta" e "Logout" na parte inferior
        bottom_container = ctk.CTkFrame(master=sidebar, fg_color="transparent")
        bottom_container.pack(side="bottom", pady=(0, 20), fill="x")

        # Botão Conta
        btn_conta = ctk.CTkButton(
            master=bottom_container,
            text="Conta",
            compound="left",
            font=self.AFACAD_BOLD15,
            fg_color=self.DOURADO_BANCO_CAPITAL,
            text_color=self.BLACK_BG,
            hover_color=self.DOURADO_BLACK,
            anchor="center",
            width=120,
            height=25,
            corner_radius=15,
            
        )
        btn_conta.pack(anchor="w", padx=10, pady=(0, 10))

        # Botão Logout
        logout_icon = Image.open("src/view/assets/icons/logout.png").resize((24, 24))
        logout_ctk = ctk.CTkImage(light_image=logout_icon, size=(24, 24))

        btn_logout = ctk.CTkButton(
            master=bottom_container,
            text="Logout",
            image=logout_ctk,
            compound="left",
            font=self.AFACAD_BOLD15,
            fg_color="transparent",
            text_color=self.BRANCO_BG,
            hover_color="#1a1a1a",
            anchor="w",
            width=120,
            height=40,
            command=self.voltarParaLogin
           
        )
        btn_logout.pack(anchor="w", padx=10)

        # Título e saudação
        label_dashboard = ctk.CTkLabel(
            master=frame2,
            text=f"Dashboard | {user['numero_conta']}",
            font=self.AFACAD_BOLD,
            text_color=self.BLACK_BG,
            fg_color="transparent"
        )
        label_dashboard.place(x=160, y=20, anchor="nw")

        user_name = user["nome"].split()

        # Container para foto + saudação (juntos)
        user_info_frame = ctk.CTkFrame(
            master=frame2,
            fg_color="transparent"
        )
        user_info_frame.place(relx=1.0, x=-20, y=20, anchor="ne")

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
            text=f"Olá, {user_name[0]} {user_name[-1]}",
            font=self.AFACAD_BOLD,
            text_color=self.BLACK_BG,
            fg_color="transparent"
        )
        label_user.pack(side="left", padx=(0, 10))  # texto primeiro, padding à direita
        label_foto.pack(side="left")               # imagem depois

        # CARD DA CONTA CORRENTE #####
        frame_card = ctk.CTkFrame(
            master=frame2,
            width=212,
            height=92,
            fg_color="transparent"
        )
        frame_card.place(x=160, y=70)

        # Label com imagem de fundo (em cima do frame)
        bg_card_image = ctk.CTkImage(
            light_image=Image.open("src/view/assets/cards/gold_card.png"),  # Certifique-se do caminho correto
            size=(210, 90)
        )
        bg_label = ctk.CTkLabel(master=frame_card, image=bg_card_image, text="", fg_color="transparent")
        bg_label.place(x=0, y=0)  # Coloca no fundo, cobrindo todo o card

        # Sobreposição direta no mesmo frame (acima do bg_label)
        # Texto "Conta corrente"
        label_tipo_conta = ctk.CTkLabel(
            master=frame_card,
            text="Conta corrente",
            font=self.AFACAD_BOLD15,
            text_color="white",
            fg_color="transparent"
        )
        label_tipo_conta.place(x=10, y=5)

        # Saldo e ícone lado a lado
        label_valor_saldo = ctk.CTkLabel(
            master=frame_card,
            text=f"R${float(user['saldo']):.2f}".replace('.', ','),
            font=self.AFACAD_BOLD15,
            text_color="white",
            fg_color="transparent"
        )
        label_valor_saldo.place(x=10, y=55)

        icone_dinheiro = ctk.CTkImage(
            light_image=Image.open("src/view/assets/icons/dinheiro.png"),
            size=(24, 24)
        )
        label_icone = ctk.CTkLabel(master=frame_card, image=icone_dinheiro, text="", fg_color="transparent")
        label_icone.place(x=170, y=55)
        # CARD DA CONTA CORRENTE #####

        
        # CARD DA CONTA DE INVESTIMENTO #####
        frame_card = ctk.CTkFrame(
            master=frame2,
            width=210,
            height=91,
            fg_color="transparent"
        )
        frame_card.place(x=423, y=70)

        # Label com imagem de fundo (em cima do frame)
        bg_card_image = ctk.CTkImage(
            light_image=Image.open("src/view/assets/cards/gold_card.png"),  # Certifique-se do caminho correto
            size=(210, 91)
        )
        bg_label = ctk.CTkLabel(master=frame_card, image=bg_card_image, text="", fg_color="transparent")
        bg_label.place(x=0, y=0)  # Coloca no fundo, cobrindo todo o card

        # Sobreposição direta no mesmo frame (acima do bg_label)
        # Texto "Conta de investimento"
        label_tipo_conta = ctk.CTkLabel(
            master=frame_card,
            text="Conta de investimento",
            font=self.AFACAD_BOLD15,
            text_color="white",
            fg_color="transparent"
        )
        label_tipo_conta.place(x=10, y=5)

        # Saldo e ícone lado a lado
        label_valor_saldo = ctk.CTkLabel(
            master=frame_card,
            text=f"R${float(user['saldo']):.2f}".replace('.', ','),
            font=self.AFACAD_BOLD15,
            text_color="white",
            fg_color="transparent"
        )
        label_valor_saldo.place(x=10, y=55)

        icone_dinheiro = ctk.CTkImage(
            light_image=Image.open("src/view/assets/icons/investir.png"),
            size=(24, 24)
        )
        label_icone = ctk.CTkLabel(master=frame_card, image=icone_dinheiro, text="", fg_color="transparent")
        label_icone.place(x=170, y=55)
        # CARD DA CONTA INVESTIMENTO #####

        # CARD DA ULTIMA TRANFERENCIA RECEBIDA #####
        frame_card = ctk.CTkFrame(
            master=frame2,
            width=210,
            height=91,
            fg_color="transparent"
        )
        frame_card.place(x=676, y=70)

        # Label com imagem de fundo (em cima do frame)
        bg_card_image = ctk.CTkImage(
            light_image=Image.open("src/view/assets/cards/green_card.png"),  # Certifique-se do caminho correto
            size=(210, 91)
        )
        bg_label = ctk.CTkLabel(master=frame_card, image=bg_card_image, text="", fg_color="transparent")
        bg_label.place(x=0, y=0)  # Coloca no fundo, cobrindo todo o card

        # Sobreposição direta no mesmo frame (acima do bg_label)
        # Texto "Conta de investimento"
        label_tipo_conta = ctk.CTkLabel(
            master=frame_card,
            text="Última tranferência recebida",
            font=self.AFACAD_BOLD15,
            text_color="white",
            fg_color="transparent"
        )
        label_tipo_conta.place(x=10, y=5)

        # Saldo e ícone lado a lado
        label_valor_saldo = ctk.CTkLabel(
            master=frame_card,
            text=f"R${float(user['saldo']):.2f}".replace('.', ','),
            font=self.AFACAD_BOLD,
            text_color="white",
            fg_color="transparent"
        )
        label_valor_saldo.place(x=10, y=55)

        icone_dinheiro = ctk.CTkImage(
            light_image=Image.open("src/view/assets/icons/transferir.png"),
            size=(24, 24)
        )
        label_icone = ctk.CTkLabel(master=frame_card, image=icone_dinheiro, text="", fg_color="transparent")
        label_icone.place(x=170, y=55)
        # CARD DA ULTIMA TRANSFERENCIA RECEBIDA #####

        # CARD DA ULTIMA TRANSFERENCIA ENVIADA #####
        frame_card = ctk.CTkFrame(
            master=frame2,
            width=210,
            height=91,
            fg_color="transparent"
        )
        frame_card.place(x=929, y=70)

        # Label com imagem de fundo (em cima do frame)
        bg_card_image = ctk.CTkImage(
            light_image=Image.open("src/view/assets/cards/red_card.png"),  # Certifique-se do caminho correto
            size=(210, 91)
        )
        bg_label = ctk.CTkLabel(master=frame_card, image=bg_card_image, text="", fg_color="transparent")
        bg_label.place(x=0, y=0)  # Coloca no fundo, cobrindo todo o card

        # Sobreposição direta no mesmo frame (acima do bg_label)
        # Texto "Conta de investimento"
        label_tipo_conta = ctk.CTkLabel(
            master=frame_card,
            text="Última tranferência enviada",
            font=self.AFACAD_BOLD15,
            text_color="white",
            fg_color="transparent"
        )
        label_tipo_conta.place(x=10, y=5)

        # Saldo e ícone lado a lado
        label_valor_saldo = ctk.CTkLabel(
            master=frame_card,
            text=f"R${float(user['saldo']):.2f}".replace('.', ','),
            font=self.AFACAD_BOLD,
            text_color="white",
            fg_color="transparent"
        )
        label_valor_saldo.place(x=10, y=55)

        icone_dinheiro = ctk.CTkImage(
            light_image=Image.open("src/view/assets/icons/transferir.png"),
            size=(24, 24)
        )
        label_icone = ctk.CTkLabel(master=frame_card, image=icone_dinheiro, text="", fg_color="transparent")
        label_icone.place(x=170, y=55)
        # CARD DA ULTIMA TRANFERENCIA ENVIADA #####



  


    def voltarParaLogin(self):
        self.app.destroy()
        self.controller.abrir_login()

    def run(self):
        self.app.mainloop()