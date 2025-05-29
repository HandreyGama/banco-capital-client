from pwinput import pwinput
from server_handler import server_requests
import re
import os
from datetime import datetime
import readchar


def validar_nome(user_nome_completo):
    return re.match(r"^[A-Za-zÀ-ÿ\'\- ]{2,}$", user_nome_completo)


def validar_email(user_email):
    return re.match(r"^[\w\.-]+@[\w\.-]+\.\w{2,}$", user_email)


def validar_cpf(user_cpf):
    return re.match(r"^\d{3}\.\d{3}\.\d{3}-\d{2}$", user_cpf)


def input_data_nascimento():
    def limpar_terminal():
        os.system("cls" if os.name == "nt" else "clear")

    def formatar_visual(data):
        visual = ""
        p = 0  # índice do placeholder

        for c in data:
            if p == 2 or p == 5:
                visual += "/"
                p += 1

            visual += c
            p += 1

        visual += "dd/mm/aaaa"[p:]
        return visual

    def validar_data_e_idade(data_str):
        try:
            nascimento = datetime.strptime(data_str, "%d/%m/%Y")
            hoje = datetime.today()

            idade = (
                hoje.year
                - nascimento.year
                - ((hoje.month, hoje.day) < (nascimento.month, nascimento.day))
            )

            if idade >= 18:
                print(f"\nData de nascimento válida: {data_str}")
                return True

            else:
                print("\n[ERRO] Usuário menor de 18 anos.")
                return False

        except ValueError:
            print("\n[ERRO] Data inválida.")
            return False

    data = ""

    while True:
        limpar_terminal()

        print("Digite sua data de nascimento:")
        print(f"[ {formatar_visual(data)} ]")

        key = readchar.readkey()

        if key in "0123456789" and len(data) < 8:
            data += key

        elif key in ["\x7f", "\b"]:  # backspace
            data = data[:-1]

        elif key == "\r":  # Enter
            if len(data) == 8:
                data_formatada = f"{data[:2]}/{data[2:4]}/{data[4:]}"
                return validar_data_e_idade(data_formatada)

            else:
                print("\n[ERRO] Data incompleta.")
                return False


class CredencialScreen:
    def __init__(self):
        pass

    def SingIn(self) -> tuple[bool, int]:
        confirmar_login = False

        while confirmar_login == False:
            cpf = input("Digite seu cpf:")
            senha = pwinput("Digite sua senha:")

            if not validar_cpf(cpf):
                print("[ERRO] CPF inválido.")

            else:
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
            if not validar_nome(user_nome_completo):
                print("[ERRO] Nome inválido.")
                continue

            user_cpf = input("Digite seu cpf (sem pontuações):")

            if len(user_cpf.strip()) == 0:
                print("[ERRO] o cpf esta vazio!")
                continue

            if user_cpf.isnumeric() == False:
                print("[ERRO] digite o cpf sem pontuações!")
                continue

            if not validar_cpf(user_cpf):
                print("[ERRO] Email inválido.")

            user_email = input("Digite seu email:")

            if len(user_email.strip()) == 0:
                print("[ERRO] o email esta vazio!")
                continue
            if not validar_email(user_email):
                print("[ERRO] Digite um email válido.")

            data_nasc = input_data_nascimento()
            user_data_nasc = data_nasc

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
                    user_nome_completo, user_cpf, user_email, user_senha, user_data_nasc
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
