menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """
# Variaveis globais:

saldo = 0 # armazena valor em conta 
limite = 500 # limite diario de saque
extrato = "" # movimentações na conta
numero_saques = 0 # quantos saques foram realizados
LIMITE_SAQUES = 3 # limite do numero de saques

while True:

    opcao = input(menu)

    if opcao == "d":
        print("Depósito")
        valor_deposito = float(input("Qual valor deseja depositar:"))
        if valor_deposito < 0:
            print("Você não pode depositar valor negativo.")
            continue
        saldo = saldo+valor_deposito
        print(f"Seu saldo é R$ {saldo}")
        extrato = extrato + f"Deposito: R$ {valor_deposito:.2f}\n"
    elif opcao == "s":
        print("Saque")
        
        if numero_saques > LIMITE_SAQUES:
            print("Limite de saques excedido")
            continue
        valor_saque = float(input("Qual valor deseja sacar:"))
        if valor_saque < 0:
            print("Digite um valor valido")
            continue
        if valor_saque > limite:
            print("Saque maior que limite permitido")
        if valor_saque > saldo:
            print("Saldo insuficiente")
        
        else:
            saldo = saldo - valor_saque
            print(f"Seu saldo é R$ {saldo}")
            numero_saques = numero_saques + 1 
            extrato = extrato + f"Saque: R$ {valor_saque:.2f}\n"
    elif opcao == "e":
        print("Extrato")
        print(f"Saldo: {saldo}")
        print(extrato)
    elif opcao == "q":
        break

else:
    print("Comando invalido")
