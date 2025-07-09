def exibir_menu(): 
    return input("""
[a] Cadastrar cliente                 
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """).strip().lower()


clientes = []


def buscar_cliente(clientes, nome):
    for cliente in clientes:
        if cliente["nome"].lower() == nome.lower():
            return cliente
    return None

def buscar_cliente_por_cpf(clientes, cpf):
    for cliente in clientes:
        if cliente["CPF"] == cpf:
            return cliente
    return None

def selecionar_cliente(clientes):
    cpf = input("Digite o CPF do cliente: ").strip().replace(".", "").replace("-", "")
    cliente = buscar_cliente_por_cpf(clientes, cpf)
    if not cliente:
        print("Cliente não encontrado.")
    return cliente

def pedir_idade():
    while True:
        idade_str = input("Digite a idade do cliente: ")
        if idade_str.isdigit() and int(idade_str) > 0:
            return int(idade_str)
        print("Idade inválida. Digite um número inteiro positivo.")

def pedir_CPF():
    while True:
        cpf = input("Digite o CPF do cliente: ").strip().replace(".", "").replace("-", "")
        if len(cpf) == 11 and cpf.isdigit():
            if buscar_cliente_por_cpf(clientes, cpf):
                print("Este CPF já está cadastrado.")
            else:
                return cpf
        else:
            print("CPF inválido. O CPF deve ter 11 dígitos numéricos.")

def pedir_endereco():
    endereco = {}
    endereco["logradouro"] = input("Digite o tipo de logradouro (ex: Rua, Avenida): ").strip().title()
    endereco["nome_rua"] = input("Digite o nome da rua: ").strip().title()
    endereco["cidade"] = input("Digite a cidade: ").strip().title()

    while True:
        estado = input("Digite o estado (sigla, ex: DF): ").strip().upper()
        if len(estado) == 2 and estado.isalpha():
            endereco["estado"] = estado
            break
        else:
            print("Estado inválido. Digite a sigla com 2 letras.")
    return endereco

def cadastrar_cliente():
    print("\nCadastro do Cliente:")
    cliente = {}
    cliente["nome"] = input("Digite o nome completo: ")
    cliente["idade"] = pedir_idade()
    cliente["CPF"] = pedir_CPF()
    cliente["endereco"] = pedir_endereco()
    cliente["conta"] = {
        "saldo": 0,
        "extrato": "",
        "numero_saques": 0
    }
    print("Cliente cadastrado com sucesso.")
    return cliente

def deposito(cliente):
    print("\nDepósito")
    valor = float(input("Qual valor deseja depositar: "))
    if valor <= 0:
        print("Valor inválido para depósito.")
    else:
        cliente["conta"]["saldo"] += valor
        cliente["conta"]["extrato"] += f"Depósito: R$ {valor:.2f}\n"
        print(f"Depósito realizado. Saldo atual: R$ {cliente['conta']['saldo']:.2f}")

def saque(cliente, limite=500, LIMITE_SAQUES=3):
    print("\nSaque")
    conta = cliente["conta"]

    if conta["numero_saques"] >= LIMITE_SAQUES:
        print("Limite de saques diários atingido.")
        return

    valor = float(input("Qual valor deseja sacar: "))
    if valor <= 0:
        print("Valor inválido.")
    elif valor > limite:
        print("Saque excede o limite permitido.")
    elif valor > conta["saldo"]:
        print("Saldo insuficiente.")
    else:
        conta["saldo"] -= valor
        conta["numero_saques"] += 1
        conta["extrato"] += f"Saque: R$ {valor:.2f}\n"
        print(f"Saque realizado. Saldo atual: R$ {conta['saldo']:.2f}")

def mostrar_extrato(cliente):
    conta = cliente["conta"]
    print("\nExtrato")
    print(conta["extrato"] if conta["extrato"] else "Nenhuma movimentação realizada.")
    print(f"Saldo atual: R$ {conta['saldo']:.2f}")
    print("=" * 30)

def remover_cliente(clientes):
    if not clientes:
        print("\nNenhum cliente cadastrado.")
        return

    nome_busca = input("Digite o nome do cliente que deseja deletar: ")
    cliente = buscar_cliente(clientes, nome_busca)

    if cliente:
        print(f"\nNome: {cliente['nome']}\nIdade: {cliente['idade']}")
        confirmacao = input(f"Tem certeza que deseja deletar {cliente['nome']}? (s/n): ").strip().lower()
        if confirmacao == "s":
            clientes.remove(cliente)
            print("Cliente deletado com sucesso.")
        else:
            print("Ação cancelada.")
    else:
        print("Cliente não encontrado.")


while True:
    opcao = exibir_menu()

    if opcao == "a":
        clientes.append(cadastrar_cliente())
    elif opcao == "d":
        cliente = selecionar_cliente(clientes)
        if cliente:
            deposito(cliente)
    elif opcao == "s":
        cliente = selecionar_cliente(clientes)
        if cliente:
            saque(cliente)
    elif opcao == "e":
        cliente = selecionar_cliente(clientes)
        if cliente:
            mostrar_extrato(cliente)
    elif opcao == "q":
        print("Encerrando o sistema.")
        break
    else:
        print("Comando inválido. Tente novamente.")

