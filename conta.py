import random
from classPessoaFisica import PessoaFisica

class Conta:
    LIMITE_SAQUE = 500
    MAX_SAQUES = 3

    def __init__(self):
        self.numero_conta = str(random.randint(10000000, 99999999))
        self.saldo = 0.0
        self.numero_saques = 0
        self.extrato = []

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: R${valor:.2f}")
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Valor inválido para depósito.")

    def sacar(self, valor):
        if valor > self.LIMITE_SAQUE:
            print("Valor acima do limite de saque.")
        elif self.numero_saques >= self.MAX_SAQUES:
            print("Limite de saques diários atingido.")
        elif valor <= 0:
            print("Valor inválido.")
        elif valor > self.saldo:
            print("Saldo insuficiente.")
        else:
            self.saldo -= valor
            self.numero_saques += 1
            self.extrato.append(f"Saque: -R${valor:.2f}")
            print(f"Saque de R${valor:.2f} realizado com sucesso!")

    def exibir_saldo(self):
        return f"Saldo atual: R${self.saldo:.2f}"

    def exibir_extrato(self):
        print(f"\nExtrato da conta {self.numero_conta}:")
        if not self.extrato:
            print("Nenhuma movimentação registrada.")
        else:
            for item in self.extrato:
                print(item)
            print(self.exibir_saldo())


            
     



