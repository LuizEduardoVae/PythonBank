menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

sim_nao = """

[y] Sim
[n] Nao

=> """


saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)
    
    if opcao == "d":
        while True:
            print( " \n Deseja depositar?")
            yes_no = input(sim_nao)

            if yes_no == "y":
                deposito = float(input("Valor do deposito:  "))
                saldo += deposito
                extrato.append(f"Depósito: {deposito}")
            else:
                break

    elif opcao == "s":
        if numero_saques < LIMITE_SAQUES:
            while True:
                print( "\nDeseja Sacar?")
                yes_no = input(sim_nao)
                saque = 0
            
                if numero_saques < LIMITE_SAQUES:
                    if yes_no == "y":
                        saque = float(input("Valor do saque:  "))
                        if saque > saldo:
                            print("\nSaldo Insuficiente")
                        elif saque > 500:
                            print("\nLimite Insuficiente")
                        else:
                            saldo -= saque
                            numero_saques += 1
                            extrato.append(f"Saque: {saque}")
                    else:
                        break
                else:
                    print(""" \nQuantidade de saques diarios atingidos 
                              \nSelecione outra opcao!
                        """)
                    break
        else:
            print(""" \nQuantidade de saques diarios atingidos 
                      \nSelecione outra opcao!
                 """)
            continue

    elif opcao == "e":
        print("\nExtrato")
        for movimentacao in extrato:
            print(movimentacao)

        print("\nSaldo Final")
        print(saldo)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")