from src.credencial_screen import credencial_shell
from src.credencial_screen.credencial_shell import CredencialScreen


class Shell:
    def __init__(self) -> None:
        self.estado = "MenuPrincipal"
        pass

    def CredencialScreen(self):
        credencial_screen = CredencialScreen()
        credencial_screen.SingUp()
        self.estado == 'MenuPrincipal'

    def SairShell(self):
        print("Saindo do banco!")
        exit()

    def MenuPrincipal(self):
        while self.estado == "MenuPrincipal":
            print("===" + " MENU PRINCIAPL " + "===")
            print(f"1. Login\n2. cadastro\n3. Sair")
            user_input = input("Digite o numero de uma das opções:")
            if user_input == "2":
                print("===" + " INICIANDO CADASTRO " + "===")
                self.estado = 'MenuPrincipal'
                self.CredencialScreen()
            if user_input == "3":
                self.SairShell()


shell = Shell()
shell.MenuPrincipal()
