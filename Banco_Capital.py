from src.view.forgou_key import EsqueciSenhaApp
from src.view.inicio import LoginApp
from src.view.dashboard import DashboardApp
from src.view.cadastro import CadastroApp
from src.view.transferencia import TransferenciaApp
from src.view.conta import ContaApp
class AppController:
    def __init__(self):
        self.telas = []  # Lista que armazena as telas
        self.abrir_login()
        self.USER_INDEX
        self.USER_EXISTS
    def abrir_login(self):
        # Fecha a tela anterior, se existir
        if self.telas:
            try:
                self.telas[-1].app.destroy()
            except Exception as e:
                print("Erro ao fechar tela anterior:", e)

        # Cria tela de login e adiciona à lista
        login = LoginApp(controller=self)
        self.telas.append(login)
        login.run()

    def abrir_dashboard(self):
        # Fecha a tela anterior
        if self.telas:
            try:
                self.telas[-1].app.destroy()
            except Exception as e:
                print("Erro ao fechar tela anterior", e)

        # Cria tela de dashboard e adiciona à lista
        dash = DashboardApp(controller=self)
        self.telas.append(dash)
        dash.run()

    def abrir_cadastro(self):
    # Fecha a tela anterior
        if self.telas:
            try:
                self.telas[-1].app.destroy()
            except Exception as e:
                print("Erro ao fechar tela anterior", e)

        # Cria tela de dashboard e adiciona à lista
        cadastro = CadastroApp(controller=self)
        self.telas.append(cadastro)
        cadastro.run()

    def abrir_transferencia(self):
    # Fecha a tela anterior
        if self.telas:
            try:
                self.telas[-1].app.destroy()
            except Exception as e:
                print("Erro ao fechar a tela anterior", e)

        # Cria tela de dashboard e adiciona à lista
        tranferencia = TransferenciaApp(controller=self)
        self.telas.append(tranferencia)
        tranferencia.run()

    def abrir_conta(self):
# Fecha a tela anterior
        if self.telas:
            try:
                self.telas[-1].app.destroy()
            except Exception as e:
                print("Erro ao fechar a tela anterior", e)

        # Cria tela de dashboard e adiciona à lista
        conta = ContaApp(controller=self)
        self.telas.append(conta)
        conta.run()

    def abrir_forgoutKey(self):
# Fecha a tela anterior
        if self.telas:
            try:
                self.telas[-1].app.destroy()
            except Exception as e:
                print("Erro ao fechar a tela anterior", e)

        # Cria tela de dashboard e adiciona à lista
        forgout = EsqueciSenhaApp(controller=self)
        self.telas.append(forgout)
        forgout.run()



if __name__ == "__main__":
    p1 = AppController()
    
