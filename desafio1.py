menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """
saldo_total = 0
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
saque = 0

while True:
    opcao = input(menu)

    if opcao == "d":
        print("Deposito\n Digite o valor a ser depositado: ")
        saldo = float(input())
        saldo_total = float(saldo_total + saldo)
        print(f"Deposito no valor de {saldo} Realizado com sucesso!")
    
    elif opcao == "s":
        print("Saque\n Informe o valor a ser sacado (limite de 500.00 por saque): ")
        saque = float(input())
        if saque <= 500 and LIMITE_SAQUES >= 1 and saque <= saldo_total:
            saldo_total = saldo_total - saque
            LIMITE_SAQUES = LIMITE_SAQUES - 1
            numero_saques = numero_saques + 1
            print(f"Saque de {saque} realizado com sucesso!")
        
        elif saque <= 500 and LIMITE_SAQUES == 0:
            print("Você já excedeu o número maximo de saques hoje!")

        elif saque <= 500 and LIMITE_SAQUES >=1 and saque > saldo_total:
            print("Seu saldo é insuficiente para realizar esse saque!")
                  
        else:
            print("Valor acima do limite permitido!")
        
    elif opcao == "e":
        print("Extrato")
        print(f"Seu saldo é de: {saldo_total}\nseu limite de saques diarios é de: {LIMITE_SAQUES}.\n você fez {numero_saques} saques hoje.  ")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

    