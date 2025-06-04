import customtkinter as ctk
from datetime import datetime
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader
from reportlab.lib import colors
import os

from src.credencial_screen.server_handler.server_requests import client_informacoes

class ExtratoApp(ctk.CTk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Extrato Bancário")
        self.geometry("1224x664")
        self.resizable(False, False)

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

        # Fonte com CTkFont
        self.AFACAD_BOLD = ctk.CTkFont(family="Afacad", size=24, weight="bold")
        self.AFACAD_REGULAR = ctk.CTkFont(family="Afacad", size=12, weight="normal")

        self.AFACAD_BOLD10 = ctk.CTkFont(family="Afacad", size=10, weight="bold")
        self.AFACAD_BOLD15 = ctk.CTkFont(family="Afacad", size=15, weight="bold")
        self.AFACAD_REGULAR20 = ctk.CTkFont(family="Afacad", size=20, weight="normal")

        self.user = client_informacoes(self.controller.USER_INDEX)
        self.transacoes = self.user["transferencias"]
        self.caminho_logo = "src/view/assets/logotype/banco-capital.png"

        self.setup_ui()

    def setup_ui(self):
        self.main_frame = ctk.CTkFrame(self, fg_color="#f8f8f8")
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Topo
        topo = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        topo.pack(fill="x", pady=10)

        ctk.CTkButton(topo, text="← Voltar", width=120, command=self.voltar,fg_color=self.BLACK_BG,text_color=self.DOURADO_BANCO_CAPITAL).pack(side="left", padx=5)
        ctk.CTkButton(topo, text="Gerar Extrato em PDF", command=self.gerar_extrato,fg_color=self.BLACK_BG,text_color=self.DOURADO_BANCO_CAPITAL).pack(side="right", padx=5)

        self.label_status = ctk.CTkLabel(topo, text="", text_color="green")
        self.label_status.pack(side="right", padx=5)

        # Lista de transações com scroll
        self.scroll_frame = ctk.CTkScrollableFrame(self.main_frame, width=1150, height=540, fg_color="white")
        self.scroll_frame.pack(pady=10, fill="both", expand=True)

        self.exibir_transacoes()

    def exibir_transacoes(self):
        for idx, transacao in enumerate(self.transacoes):
            try:
                data_raw = transacao[2]
                data = datetime.fromisoformat(data_raw).strftime("%d/%m/%Y") if 'T' in data_raw else data_raw[:10]
                descricao = transacao[3] if len(transacao) > 3 else "Descrição indisponível"
                valor_bruto = transacao[1]

                sinal = -1 if '-' in valor_bruto else 1
                valor_float = sinal * float(valor_bruto.replace("R$", "").replace("+", "").replace("-", "").strip())
                valor_str = f"R$ {valor_float:.2f}"
                cor_valor = "red" if valor_float < 0 else "green"

                frame = ctk.CTkFrame(self.scroll_frame, fg_color="#f0f0f0", corner_radius=12)
                frame.pack(fill="x", pady=6, padx=10)

                ctk.CTkLabel(frame, text=f"Data: {data}", anchor="w",font=self.AFACAD_REGULAR, text_color=self.BLACK_BG).pack(anchor="w", padx=10, pady=2)
                ctk.CTkLabel(frame, text=f"Descrição: {descricao}", anchor="w",font=self.AFACAD_REGULAR, text_color=self.BLACK_BG).pack(anchor="w", padx=10, pady=2)
                ctk.CTkLabel(frame, text=f"Valor: {valor_str}", text_color=cor_valor, anchor="w",font=self.AFACAD_REGULAR).pack(anchor="w", padx=10, pady=2)

               
                if len(transacao) >= 5:
                    destinatario = transacao[4]
                    nome_usuario = self.user["nome"]
                    if destinatario and destinatario != nome_usuario:
                        ctk.CTkLabel(frame, text=f"Destinatário: {destinatario}", anchor="w",font=self.AFACAD_BOLD15, text_color=self.BLACK_BG).pack(anchor="w", padx=10, pady=2)

                ctk.CTkButton(frame, text="📄 Baixar Comprovante", width=180,
                            command=lambda t=transacao: self.gerar_comprovante_individual(t),fg_color=self.BLACK_BG,text_color=self.DOURADO_BANCO_CAPITAL).pack(side="right", padx=10, pady=5)
                            

            except Exception as e:
                print(f"Erro ao exibir transação {idx}: {e}")


    def gerar_extrato(self):
        try:
            caminho = self.gerar_pdf_extrato(self.caminho_logo)
            self.label_status.configure(text=f"PDF salvo em: {caminho}", text_color="green")
        except Exception as e:
            self.label_status.configure(text=f"Erro: {e}", text_color="red")

    def gerar_comprovante_individual(self, transacao):
        user_name = self.user["nome"].split()
        base_name = f"{user_name[0]}_{user_name[-1]}_comprovante"
        pasta = "src/view/assets/extratos"
        os.makedirs(pasta, exist_ok=True)

        indice = 1
        while True:
            path = os.path.join(pasta, f"{base_name}_{indice}.pdf")
            if not os.path.exists(path):
                break
            indice += 1

        c = canvas.Canvas(path, pagesize=A4)
        c.setFont("Helvetica-Bold", 12)
        c.drawString(40, 800, "Comprovante de Transação")
        c.setFont("Helvetica", 10)

        try:
            c.drawString(40, 780, f"Nome: {self.user['nome']}")
            c.drawString(40, 765, f"Conta: {self.user['numero_conta']}")
            c.drawString(40, 750, f"Data: {transacao[2][:10]}")
            c.drawString(40, 735, f"Valor: {transacao[1]}")
            c.drawString(40, 720, f"Descrição: {transacao[3]}")
        except:
            c.drawString(40, 735, "Erro ao processar dados da transação.")

        c.save()
        self.label_status.configure(text=f"Comprovante salvo em: {path}", text_color="green")

    def gerar_pdf_extrato(self, logo_path):
        # Mesma função que já está no seu código anterior (mantida sem alterações)
        ...

    def voltar(self):
        self.destroy()
        self.controller.abrir_dashboard()

    def run(self):
        self.mainloop()
