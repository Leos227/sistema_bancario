from classPessoaFisica import PessoaFisica
from conta import Conta

def exibir_menu():
    print("""
====== MENU ======
[1] Cadastrar cliente
[2] Abrir conta        
[3] Depositar
[4] Sacar
[5] Listar contas
[6] Ver extrato
[0] Sair
""")
    return input("Escolha uma opção: ").strip()


clientes = []

while True:
    opcao = exibir_menu()

    if opcao == "1":
        nome = input("Nome: ").strip()
        cpf = input("CPF: ").strip()
        data_de_nascimento = input("Data de nascimento (dd/mm/aaaa): ").strip()
        cliente = PessoaFisica(nome, data_de_nascimento, cpf)
        clientes.append(cliente)
        print(f"\nCliente {nome} cadastrado com sucesso!\n")

    elif opcao == "2":
        cpf = input("CPF do cliente: ").strip()
        cliente = next((c for c in clientes if c.cpf == cpf), None)
        if cliente:
            conta = Conta()
            cliente.adicionar_conta(conta)
            print(f"\nConta {conta.numero_conta} criada para {cliente.nome}.\n")
        else:
            print("Cliente não encontrado.")

    elif opcao == "3":
        cpf = input("CPF do cliente: ").strip()
        cliente = next((c for c in clientes if c.cpf == cpf), None)
        if cliente and cliente.contas:
            conta = cliente.contas[0]
            valor_str = input("Valor para depósito: R$").replace(',', '.')
            valor = float(valor_str)
            conta.depositar(valor)
        else:
            print("Cliente ou conta não encontrado.")

    elif opcao == "4":
        cpf = input("CPF do cliente: ").strip()
        cliente = next((c for c in clientes if c.cpf == cpf), None)
        if cliente and cliente.contas:
            conta = cliente.contas[0]
            valor_str = input("Valor para depósito: R$").replace(',', '.')
            valor = float(valor_str)
            conta.sacar(valor)
        else:
            print("Cliente ou conta não encontrado.")

    elif opcao == "5":
        if not clientes:
            print("Nenhum cliente cadastrado.")
        else:
            print("\n=== LISTA DE CONTAS EXISTENTES ===")
            for cliente in clientes:
                if cliente.contas:
                    for conta in cliente.contas:
                        print(f"Cliente: {cliente.nome} | CPF: {cliente.cpf} | Conta: {conta.numero_conta} | Saldo: R${conta.saldo:.2f}")
                else:
                    print(f"Cliente: {cliente.nome} | CPF: {cliente.cpf} | Sem contas cadastradas.")
    

    elif opcao == "6":
        cpf = input("CPF do cliente: ").strip()
        cliente = next((c for c in clientes if c.cpf == cpf), None)
        if cliente and cliente.contas:
            conta = cliente.contas[0]
            conta.exibir_extrato()
        else:
            print("Cliente ou conta não encontrado.")

    elif opcao == "0":
        print("Encerrando o sistema. Até logo!")
        break

    else:
        print("Opção inválida. Tente novamente.")

