
menu = ("""
    ================= MENU ==================
    
    1 - Depositar
    2 - Sacar
    3 - Extrato
    4 - Sair
    
    Selecione uma opção númerica: """)

QUANTIDADE_LIMITE_SAQUE = 3
VALOR_SAQUE_LIMITE_MAXIMO = 500

saldo = 0
extrato = ""
numero_saques = 0

while True:
    opcao = int(input(menu))


    if opcao == 1:
        valor_a_depositar = float(input("Digite o valor que deseja DEPOSITAR: R$"))

        if valor_a_depositar <= 0:
            print(f"Não foi possível adicionar R$ {valor_a_depositar:.2f}")
            continue

        saldo += valor_a_depositar
        extrato += f"\nDEPÓSITO: R${valor_a_depositar:.2f}"
        print(f"Saldo de R${valor_a_depositar:.2f}. Adicionado com sucesso!")
    
    elif opcao == 2:

        if numero_saques == QUANTIDADE_LIMITE_SAQUE:
            print("Limite de saques diários atingido.")
            continue

        valor_sacado = float(input("Digite o valor que deseja SACAR: R$"))

        if valor_sacado > VALOR_SAQUE_LIMITE_MAXIMO:
            print("Não é possível sacar mais que R$500,00.")
            continue

        if valor_sacado > saldo:
            print("Saldo insuficiente.")
            continue

        if valor_sacado < 0:
            print("Valor inválido.")
            continue

        numero_saques += 1
        saldo -= valor_sacado
        extrato += f"\nSAQUE: R${valor_sacado:.2f}"
        
        print(f"Valor de R${valor_sacado:.2f} sacado com sucesso!")

    elif opcao == 3:
        print("\n======== EXTRATO ========")
        if extrato == "":
            print("Nenhuma movimentação realizada.")
        else:
            print(extrato)

        print(f"\nSaldo disponível: R${saldo:.2f}")
        print("===========================\n")


    elif opcao == 4:
        print("Sistema encerrado.")
        break

    else:
        print("Opção inválida. Tente novamente.")
    print("=========================================")

    