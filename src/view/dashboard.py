
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
        
        self.user = client_informacoes(self.controller.USER_INDEX)
        self.transacoes = self.user["transferencias"]

        # Fonte com CTkFont
        self.AFACAD_BOLD = ctk.CTkFont(family="Afacad", size=24, weight="bold")
        self.AFACAD_REGULAR = ctk.CTkFont(family="Afacad", size=12, weight="normal")

        self.AFACAD_BOLD10 = ctk.CTkFont(family="Afacad", size=10, weight="bold")
        self.AFACAD_BOLD15 = ctk.CTkFont(family="Afacad", size=15, weight="bold")
        self.AFACAD_REGULAR20 = ctk.CTkFont(family="Afacad", size=20, weight="normal")

        # Frame principal
        frame = ctk.CTkFrame(master=self.app)
        frame.pack(fill="both", expand=True)

        frame2 = ctk.CTkFrame(master=frame, fg_color="white", corner_radius=0)
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
        def criar_botao_sidebar(master, texto, caminho_icon, cor_fundo="transparent",command=None):

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

        # Container central para os botões
        middle_container = ctk.CTkFrame(master=sidebar, fg_color="transparent")
        middle_container.pack(expand=True)

        # Botões do meio
        btn_transferir = criar_botao_sidebar(middle_container, "Transferir", "src/view/assets/icons/transferir.png",command=self.irParaTransferencia)
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
            command=self.irParaConta
            
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
            text=f"Dashboard | {self.user['numero_conta']}",
            font=self.AFACAD_BOLD,
            text_color=self.BLACK_BG,
            fg_color="transparent"
        )
        label_dashboard.place(x=160, y=20, anchor="nw")

        user_name = self.user["nome"].split()

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

        card1 = ctk.CTkFrame(frame2, width=200, height=120, corner_radius=20, fg_color=self.BLACK_BG)
        card1.place(x=160, y=70)

        icon1 = ctk.CTkImage(Image.open("src/view/assets/icons/dinheiro2.png"), size=(28, 22))
        ctk.CTkLabel(card1, image=icon1, text="").place(x=15, y=15)
        ctk.CTkLabel(card1, text="Conta corrente", font=self.AFACAD_REGULAR, text_color="white").place(x=60, y=20)
        ctk.CTkLabel(card1, text=f"R${self.user['saldo'].replace('.',',')}", font=("Arial", 20, "bold"), text_color="white").place(x=15, y=55)
        ctk.CTkLabel(card1, text="Economize para poder crescer!", font=("Arial", 11), text_color="#cbd5e1").place(x=15, y=90)


         # CARD 2 - Avg. Order Amount
        card2 = ctk.CTkFrame(frame2, width=200, height=120, corner_radius=20, fg_color=self.BRANCO_BG_CARD)
        card2.place(x=423, y=70)

        icon2 = ctk.CTkImage(Image.open("src/view/assets/icons/investir3.png"), size=(28, 22))
        ctk.CTkLabel(card2, image=icon2, text="").place(x=15, y=15)
        ctk.CTkLabel(card2, text="Carteira de investimento", font=self.AFACAD_REGULAR, text_color="black").place(x=60, y=20)
        ctk.CTkLabel(card2, text=f"R${self.user['saldo'].replace('.',',')}", font=("Arial", 20, "bold"), text_color="black").place(x=15, y=55)
        ctk.CTkLabel(card2, text="↑", font=("Arial", 13, "bold"), text_color="#f87171").place(x=140, y=60)
        ctk.CTkLabel(card2, text="A pressa é inimiga da perfeição!)", font=("Arial", 11), text_color="#94a3b8").place(x=15, y=90)

        ultima_recebida = None
        for t in reversed(self.transacoes):                             # percorre de trás-para-frente
            if t[1].startswith("+"):                                   # recebida tem sinal +
                ultima_recebida = t
                break

        if ultima_recebida:
            # “+200” -> “R$200,00”
            valor_bruto = ultima_recebida[1][1:]                        # remove o +
            valor_formatado = f"R${valor_bruto.replace('.', ',')}"
        else:
            valor_formatado = "R$0,00"

        # CARD 3 -
        card3 = ctk.CTkFrame(frame2, width=200, height=120,
                             corner_radius=20, fg_color=self.BRANCO_BG_CARD)
        card3.place(x=676, y=70)

        icon3 = ctk.CTkImage(Image.open("src/view/assets/icons/transferir2.png"), size=(28, 22))
        ctk.CTkLabel(card3, image=icon3, text="").place(x=15, y=15)
        ctk.CTkLabel(card3, text="Última transferência recebida",
                     font=self.AFACAD_REGULAR, text_color="black").place(x=60, y=20)

        # <<< ESTA linha usa o valor calculado >>>
        ctk.CTkLabel(card3, text=valor_formatado,
                     font=("Arial", 20, "bold"),
                     text_color="black").place(x=15, y=55)

        ctk.CTkLabel(card3, text="↓", font=("Arial", 13, "bold"),
                     text_color="#4ade80").place(x=140, y=60)

        if ultima_recebida:
            data_txt = ultima_recebida[2]                               # AAAA-MM-DD
            legenda = f"Recebido em {data_txt}"
        else:
            legenda = "Nenhuma transferência recebida"
        ctk.CTkLabel(card3, text=legenda, font=("Arial", 11),
                     text_color="#94a3b8").place(x=15, y=90)

        # CARD 4 -
        card4 = ctk.CTkFrame(frame2, width=200, height=120, corner_radius=20, fg_color=self.BRANCO_BG_CARD)
        card4.place(x=929, y=70)

        icon4 = ctk.CTkImage(Image.open("src/view/assets/icons/transferir2.png"), size=(28, 22))
        ctk.CTkLabel(card4, image=icon4, text="").place(x=15, y=15)
        ctk.CTkLabel(card4, text="Última transferência enviada", font=self.AFACAD_REGULAR, text_color="black").place(x=60, y=20)
        ctk.CTkLabel(card4, text=f"R${self.user['saldo'].replace('.',',')}", font=("Arial", 20, "bold"), text_color="black").place(x=15, y=55)
        ctk.CTkLabel(card4, text="+3.8% ↑", font=("Arial", 13, "bold"), text_color="#4ade80").place(x=140, y=60)
        ctk.CTkLabel(card4, text="Compared to ($8,569 last year)", font=("Arial", 11), text_color="#94a3b8").place(x=15, y=90)


  

    def irParaConta(self):
        self.app.destroy()
        self.controller.abrir_conta()
    def voltarParaLogin(self):
        self.app.destroy()
        self.controller.abrir_login()
    def irParaTransferencia(self):
        self.app.destroy()
        self.controller.abrir_transferencia()

    def run(self):
        self.app.mainloop()