from pwinput import pwinput
from .server_handler import server_requests


class CredencialScreen:
    def __init__(self):
        pass

    def SingIn(self) -> tuple[bool, int]:
        confirmar_login = False

        while confirmar_login == False:
            cpf = input("Digite seu cpf:")
            senha = pwinput("Digite sua senha:")
            checar_informacoes_login = input("As informações estão corretas?(S/N):")

            if checar_informacoes_login.lower() == "s":
                confirmar_login = True
                is_client_in_database, client_index = server_requests.client_login(
                    cpf, senha
                )
                return is_client_in_database, client_index
            elif checar_informacoes_login.lower() == "n":
                continuar_login = input("Deseja continuar o login?(S/N):")

                if continuar_login.lower() == "s":
                    continue

                elif continuar_login.lower() == "n":
                    break

                else:
                    print("[ERRO] digite uma opção valida!")
            else:
                print("[ERRO] digite uma opção valida!")
        return False, 0

    def SingUp(self):
        confirmar_registro = False
        while confirmar_registro == False:
            user_nome_completo = input("Digite seu nome completo:")
            if len(user_nome_completo.strip()) == 0:
                print("[ERRO] o nome do usuario esta vazio!")
                continue
            user_cpf = input("Digite seu cpf (sem pontuações):")
            if len(user_cpf.strip()) == 0:
                print("[ERRO] o cpf esta vazio!")
                continue
            if user_cpf.isnumeric() == False:
                print("[ERRO] digite o cpf sem pontuações!")
                continue
            user_email = input("Digite seu email:")
            if len(user_email.strip()) == 0:
                print("[ERRO] o email esta vazio!")
                continue
            user_senha = pwinput(prompt="Digite sua senha:", mask="*")
            user_confirmar_senha = pwinput(prompt="Digite sua senha:", mask="*")
            if len(user_senha.strip()) == 0 or len(user_confirmar_senha.strip()) == 0:
                print("[ERRO] o campo das senhas esta vazio!")
                continue
            if user_senha != user_confirmar_senha:
                print("[ERRO] as senhas não conhecidem!")
                continue
            user_confirmar_registro = input("Os dados inseridos estão corretos?:(S/N)")

            if user_confirmar_registro.lower() == "s":
                confirmar_registro = True
                server_requests.client_register(
                    user_nome_completo, user_cpf, user_email, user_senha
                )
                print("Terminando registro!")
                break

            elif user_confirmar_registro.lower() == "n":
                refazer_registro = input("Gostaria de refazer o registro?:(S/N)")

                if refazer_registro.lower() == "s":
                    continue

                elif refazer_registro.lower() == "n":
                    print("voltando ao menu principal")
                    break
            elif (
                user_confirmar_registro.lower() != "n"
                or user_confirmar_registro.lower() != "s"
            ):
                print("[ERRO] digite um comando valido!")
