def menu():
    menu = ("""
    ================= MENU ==================
    
    1 - Depositar
    2 - Sacar
    3 - Extrato
    4 - Criar Usuário
    5 - Criar Conta
    6 - Sair
    
    Selecione uma opção númerica: """)

    return menu

def depositarValor(valor_depositado, saldo, /):

    if valor_depositado <= 0:
        print(f"Não foi possível adicionar R$ {valor_depositado:.2f}")

    else:
        saldo += valor_depositado
    
    return saldo

def sacarValor(*, valor_saque, saldo, VALOR_SAQUE_LIMITE_MAXIMO):
    if valor_saque > VALOR_SAQUE_LIMITE_MAXIMO:
        print("Não é possível sacar mais que R$500,00.")
        return saldo, False

    elif valor_saque > saldo:
        print("Saldo insuficiente.")
        return saldo, False

    elif valor_saque < 0:
        print("Valor inválido.")
        return saldo, False

    saldo -= valor_saque
    print(f"Valor de R${valor_saque:.2f} sacado com sucesso!")
    return saldo, True

def mostrarExtrato(saldo, /, *, extrato):
    print("\n======== EXTRATO ========")
    print("Nenhuma movimentação realizada." if not extrato else extrato)
    print(f"\nSaldo disponível: R${saldo:.2f}")
    print("===========================\n")

def criarUsuario(contasUsuarios: list): 
    cpf = input("Digite seu CPF (apenas números): ")
    usuario = filtrar_usuario(cpf, contasUsuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return
    
    nome = input("Informe seu nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    
    contasUsuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

def criar_conta(agencia, numero_conta, contasUsuarios):
    cpf = input("Digite seu CPF (apenas números): ")
    usuario = filtrar_usuario(cpf, contasUsuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")


def filtrar_usuario(cpf, contasUsuario):
    usuario_filtrado = [usuario for usuario in contasUsuario if usuario["cpf"] == cpf]
    return usuario_filtrado[0] if usuario_filtrado else None

def main():
    QUANTIDADE_LIMITE_SAQUE = 3
    VALOR_SAQUE_LIMITE_MAXIMO = 500
    AGENCIA = "0001"

    saldo = 0
    extrato = ""
    numero_saques = 0
    contasUsuarios = []
    contasCorrentes = []


    while True:
        opcao =  int(input(menu()))


        if opcao == 1:
            valor_a_depositar = float(input("Digite o valor que deseja DEPOSITAR: R$"))

            saldo = depositarValor(valor_a_depositar, saldo)
            extrato += f"\nDEPÓSITO: R${valor_a_depositar:.2f}"

            print(f"Saldo de R${valor_a_depositar:.2f}. Adicionado com sucesso!")
        
        elif opcao == 2:

            if numero_saques == QUANTIDADE_LIMITE_SAQUE:
                print("Limite de saques diários atingido.")
                continue

            valor_saque = float(input("Digite o valor que deseja SACAR: R$"))

            saldo, is_saque_realizado = sacarValor(valor_saque=valor_saque, saldo=saldo, VALOR_SAQUE_LIMITE_MAXIMO=VALOR_SAQUE_LIMITE_MAXIMO)

            if is_saque_realizado:
                numero_saques += 1
                extrato += f"\nSAQUE: R${valor_saque:.2f}"

        elif opcao == 3:
            mostrarExtrato(saldo, extrato=extrato)
        
        elif opcao == 4:
            criarUsuario(contasUsuarios)

        elif opcao == 5:
            numero_conta = len(contasCorrentes) + 1
            novaConta = criar_conta(AGENCIA, numero_conta, contasUsuarios)

            if novaConta:
                contasCorrentes.append(novaConta)

        elif opcao == 6:
            print("Sistema encerrado.")
            break

        else:
            print("Opção inválida. Tente novamente.")
        print("=========================================")


main()