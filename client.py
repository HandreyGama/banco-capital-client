from src import credencial_screen
from src.credencial_screen import credencial_shell
from src.credencial_screen.credencial_shell import CredencialScreen
from src.credencial_screen.server_handler import server_requests
from src.bank_screen_options import bank_menu


class Shell:
    def __init__(self) -> None:
        self.estado = "MenuPrincipal"
        pass

    def CredencialScreen(self):
        credencial_screen = CredencialScreen()
        credencial_screen.SingUp()
        self.estado = "MenuPrincipal"

    def LoginScreen(self):
        credencial_screen = CredencialScreen()
        while True:
            client_information = credencial_screen.SingIn()
            print(client_information)
            if client_information[0] == True:
                bank_menu.user_index = client_information[1]
                bank_menu.main()
                break
            elif client_information[0] == False:
                print("[ERRO] cpf ou senha invalidas!")
                pass
        self.estado = "BankMenu"

    def SairShell(self):
        print("Saindo do banco!")
        exit()

    def MenuPrincipal(self):
        while self.estado == "MenuPrincipal":
            print("===" + " MENU PRINCIPAL " + "===")
            print(f"1. Login\n2. cadastro\n3. Sair")
            user_input = input("Digite o numero de uma das opções:")
            if user_input == "1":
                print("===" + " INICIANDO LOGIN " + "===")
                self.estado = "LOGIN"
                self.LoginScreen()

            if user_input == "2":
                print("===" + " INICIANDO CADASTRO " + "===")
                self.estado = "CADASTRO"
                self.CredencialScreen()
            if user_input == "3":
                server_requests.close_conection()
                self.SairShell()

    def run(self):
        self.app.mainloop()


if __name__ == "__main__":
    while True:
        shell = Shell()
        shell.MenuPrincipal()
