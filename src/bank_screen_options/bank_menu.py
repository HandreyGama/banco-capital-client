from ..credencial_screen.server_handler.server_requests import *

user_index = 0


def main():
    while True:
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
            status = client_tranferencia(user_index, valor_transferencia, numero_conta)
            if status == True:
                break
            else:
                print("[ERRO] transferencia não foi bem sucessida")

        pass
    elif user_input == "3":
        pass
    elif user_input == "4":
        pass
    elif user_input == "5":
        pass
    elif user_input == "6":
        pass
    else:
        print("Digite uma opção valida!")


if __name__ == "__main__":
    while True:
        main()
