from inicio import LoginApp
from dashboard import Dashboard

class AppController:
    def __init__(self):
        self.telas = []  # Lista que armazena as telas
        self.abrir_login()

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
                print("Erro ao fechar tela de login:", e)

        # Cria tela de dashboard e adiciona à lista
        dash = Dashboard()
        self.telas.append(dash)
        dash.run()

if __name__ == "__main__":
    AppController()
