from ..credencial_screen.server_handler.server_requests import *
from ..gerar_grafico_transferencias import *
import pwinput

user_index = 0

exit_program = False


def main():
    while exit_program == False:
        bank_menu()


def bank_menu():
    print("===" + " MENU DO USUARIO " + "===")
    print("""
    1. Exibir informações da conta\n 
    2. Realizar transferência\n 
    3. Verificar saldo da conta\n 
    4. Extrato\n 
    5. Atuaizar cadastro\n 
    6. Sair\n 
    """)
    user_input = input("Digite uma das opções acima:")
    if user_input == "1":
        user_info = client_informacoes(user_index)
        print("=" * 6 + " DADOS BANCARIOS DO USUARIO " + "=" * 6)
        print("\n")
        for i in user_info:
            if i == "transferencias" or i == "foto_perfil":
                continue
            print(f"* {i}: {user_info[i]}")
        print("\n")
    elif user_input == "2":
        print("=" * 6 + " INICIANDO TRANSFERÊNCIA " + "=" * 6)
        print("")
        saldo = (client_informacoes(user_index))["saldo"]
        while True:
            valor_transferencia_invalido = False

            numero_conta = input("Informe o número de conta:")
            if numero_conta.isnumeric() == False:
                print("[ERRO] Número de conta inválido, digite novamente.")
                continue
            valor_transferencia = input("Informe o valor da transferência:")
            try:
                float(valor_transferencia)
            except:
                valor_transferencia_invalido = True
            if valor_transferencia_invalido == True:
                print("[ERRO] Valor inválido, digite novamente.")
                continue
            transferencia_target = client_get_user_target(numero_conta)
            print(
                "Os dados da transferencia estão correto?:\n"
                + "=" * 6
                + " DADOS DA TRANSFERENCIA"
                + "=" * 6
                + "\n"
                + f"* nome:{transferencia_target}\n"
                + f"* Valor:{valor_transferencia}"
            )
            confirmar_transferencia = input("confirmar transferencia(s/n):")
            if confirmar_transferencia.lower() == "s":
                status = client_tranferencia(
                    user_index, valor_transferencia, numero_conta, saldo
                )
                if status == True:
                    break
                else:
                    print("[ERRO] transferencia não foi bem sucessida")
            elif confirmar_transferencia.lower() == "n":
                recomecar_tranferencia = input(
                    "Gostaria de digitar os dados novamente(s/n)?:"
                )
                if recomecar_tranferencia.lower() == "s":
                    continue
                elif recomecar_tranferencia.lower() == "n":
                    print("=" * 6 + " ABORTANDO TRANSFERENCIA " + "=" * 6)
                    break

        pass
    elif user_input == "3":
        client_gerar_grafico_transferencias(user_index)
        client_gerar_grafico_saldo(user_index)
        pass
    elif user_input == "4":
        print("=" * 6 + " EXTRATO DA CONTA " + 6 * "=")
        print("")
        user_extrato = client_extrato(user_index)
        for e in reversed(user_extrato):
            print("#" * 6 + f" DATA: {e[2]} " + "#" * 6)
            print("-" * 12)
            print(f"* CONTA:{e[0]}")
            print(f"* VALOR:{e[1]}")
            print(f"* NOME DO DESTINATÁRIO:{e[-1]}")
            print(f"* TIPO DE TRANSFERÊNCIA:{e[-2]}")
            print("-" * 12 + " FIM DO DIA")
            print("")

        pass
    elif user_input == "5":
        campo_mudança_client = input(
            "Digite o numero do campo que vc quer mudar:\n1.email\n2.senha\n3.numero de telefone\n:"
        )
        if campo_mudança_client == "1":
            user_new_email = input("Digite seu novo endereço de email:")
            client_update_info("email", user_new_email, user_index)
        elif campo_mudança_client == "2":
            user_new_senha = pwinput.pwinput("Digite sua nova senha:")
            client_update_info("senha", user_new_senha, user_index)

        elif campo_mudança_client == "3":
            user_new_telefone = input("Digite seu novo telefone:")
            client_update_info("telefone", user_new_telefone, user_index)
        else:
            print("[ERRO] input invalido! escolha uma das opções listadas!")
        pass
    elif user_input == "6":
        global exit_program
        print("-" * 6 + " SAINDO DO BANCO " + "-" * 6)
        exit_program = True
        exit()

    else:
        print("Digite uma opção valida!")


if __name__ == "__main__":
    while exit_program == False:
        main()
