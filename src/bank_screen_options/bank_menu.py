def main():
    while True:
        bank_menu()

def bank_menu():
    print("===" + " MENU DO USUARIO " + "===")
    print("""
    1. informações da conta\n 
    2. fazer transferencia\n 
    3. saldo\n 
    4. extrato bancario\n 
    5. mudar informações da conta\n 
    6. sair\n 
    """)
    user_input = input("Digite uma das opções acima:")
    if user_input == "1":
        pass
    elif user_input == "2":
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
