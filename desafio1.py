def exibir_menu():
    menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    => """
    return input(menu).strip().lower()

def depositar(saldo_total):
    valor = float(input("Digite o valor a ser depositado: "))
    saldo_total += valor
    print(f"Depósito no valor de {valor:.2f} realizado com sucesso!")
    return saldo_total

def sacar(saldo_total, numero_saques, LIMITE_SAQUES):
    valor = float(input("Informe o valor a ser sacado (limite de 500.00 por saque): "))
    if valor > 500:
        print("Valor acima do limite permitido!")
    elif numero_saques >= LIMITE_SAQUES:
        print("Você já excedeu o número máximo de saques hoje!")
    elif valor > saldo_total:
        print("Seu saldo é insuficiente para realizar esse saque!")
    else:
        saldo_total -= valor
        numero_saques += 1
        print(f"Saque de {valor:.2f} realizado com sucesso!")
    return saldo_total, numero_saques

def exibir_extrato(saldo_total, numero_saques, LIMITE_SAQUES):
    print(f"Seu saldo é de: {saldo_total:.2f}\n"
          f"Seu limite de saques diários é de: {LIMITE_SAQUES - numero_saques}\n"
          f"Você fez {numero_saques} saques hoje.")

def main():
    saldo_total = 0
    numero_saques = 0
    LIMITE_SAQUES = 3

    while True:
        opcao = exibir_menu()

        if opcao == 'd':
            saldo_total = depositar(saldo_total)
        elif opcao == 's':
            saldo_total, numero_saques = sacar(saldo_total, numero_saques, LIMITE_SAQUES)
        elif opcao == 'e':
            exibir_extrato(saldo_total, numero_saques, LIMITE_SAQUES)
        elif opcao == 'q':
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()
