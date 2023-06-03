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

def sacar(*, saque, numero_saques, saldo, extrato):
    
    if saque > saldo:
        print("\nSaldo Insuficiente")
    elif saque > limite:
        print("\nLimite Insuficiente")
    elif numero_saques >= LIMITE_SAQUES:
        print("""\nQuantidade de saques diários atingidos
                  \nSelecione outra opção!
             """)
    else:
        saldo -= saque
        numero_saques += 1
        extrato.append(f"Saque: {saque}")

    return saldo, numero_saques

def despositar(deposito,saldo,extrato,/):

    saldo += deposito
    extrato.append(f"Depósito: {deposito}")

    return saldo

        
def extrato_bancario(saldo,/,*,extrato):
    for movimentacao in extrato:
            print(movimentacao)

    print("\nSaldo Final:")
    print(saldo)



while True:

    opcao = input(menu)
    
    if opcao == "d":
        while True:
            print( " \nDeseja depositar?")
            yes_no = input(sim_nao)

            if yes_no == "y":
                deposito = float(input("Valor do deposito:  "))
                saldo = despositar(deposito,saldo,extrato)
                
            else:
                break

    elif opcao == "s":
            
            while True:
                print( "\nDeseja Sacar?")
                yes_no = input(sim_nao)
                saque = 0
                
                if yes_no == "y":
                    saque = float(input("Valor do saque:  "))
                    saldo, numero_saques= sacar(saque=saque, numero_saques=numero_saques, saldo=saldo,extrato=extrato)
                else:
                    break


    elif opcao == "e":
         while True:
                print( "\n======== Deseja ver o Extrato? ========")
                yes_no = input(sim_nao)
                
                if yes_no == "y":
                    print("\n======== Extrato ========")
                    extrato_bancario(saldo, extrato=extrato)
                else:
                    break
     

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")