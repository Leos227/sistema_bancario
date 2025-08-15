class PessoaFisica:
    def __init__(self, nome, data_de_nascimento, cpf):
        self.nome = nome
        self.data_de_nascimento = data_de_nascimento
        self.cpf = cpf
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)

    def __str__(self):
        if self.contas:
            return f"{self.nome} | CPF: {self.cpf} | Conta(s): {[conta.numero_conta for conta in self.contas]}"
        else:
            return f"{self.nome} | CPF: {self.cpf} | Nenhuma conta cadastrada"

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}: ({self.cpf})>"
