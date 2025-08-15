import random
from datetime import datetime

from contaInterator import ContaIterator
from log_transacao import log_transacao


class Deposito:
    def __init__(self, valor):
        self.valor = valor


class Saque:
    def __init__(self, valor):
        self.valor = valor


class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "Tipo": transacao.__class__.__name__,
                "Valor": transacao.valor,
                "Data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            }
        )

    def gerar_relatorio(self, tipo=None):
        for transacao in self._transacoes:
            if tipo is None or transacao["Tipo"].lower() == tipo.lower():
                yield f'{transacao["Tipo"]}: R${transacao["Valor"]:.2f} em {transacao["Data"]}'

    def __iter__(self):
        return ContaIterator(self._transacoes)

    def transacoes_do_dia(self):
        data_atual = datetime.now().date()
        return [
            transacao
            for transacao in self._transacoes
            if datetime.strptime(transacao["Data"], "%d-%m-%Y %H:%M:%S").date()
            == data_atual
        ]


class Conta:
    LIMITE_SAQUE = 500
    MAX_SAQUES = 3

    @log_transacao
    def __init__(self, pessoa_fisica):

        self.pessoa = pessoa_fisica
        self.numero_conta = str(random.randint(10000000, 99999999))
        self.saldo = 0.0
        self.numero_saques = 0
        self.extrato = []
        self.agencia = 13
        self.historico = Historico()

        self.pessoa.adicionar_conta(self)

    def __repr__(self):
        return f"<Conta: ('{self.agencia}','{self.numero_conta}','{self.pessoa.nome}')>"

    def __str__(self):
        return f"""
                Agência:\t{self.agencia}
                C/C:\t\t{self.numero_conta}
                Titular:\t{self.pessoa.nome}
                """

    @log_transacao
    def depositar(self, valor):
        if valor > 0:
            self.data = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            self.saldo += valor
            self.extrato.append(f"Depósito: R${valor:.2f} em {self.data}")
            self.historico.adicionar_transacao(Deposito(valor))
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Valor inválido para depósito.")

    @log_transacao
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
            self.data = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            self.extrato.append(f"Saque: -R${valor:.2f} em {self.data}")
            self.historico.adicionar_transacao(Saque(valor))
            print(f"Saque de R${valor:.2f} realizado com sucesso!")

    @log_transacao
    def exibir_saldo(self):
        return f"Saldo atual: R${self.saldo:.2f}"

    @log_transacao
    def exibir_extrato(self):
        print(f"\nExtrato da conta {self.numero_conta}:")
        if not self.extrato:
            print("Nenhuma movimentação registrada.")
        else:
            for item in self.extrato:
                print(item)
            print(self.exibir_saldo())
