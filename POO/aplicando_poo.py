class ContaCorrente:

    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0

    def consultar_saldo(self):
        print(f"Seu saldo atual é de R${self.saldo:.2f}")

    def depositar(self, valor):
        self.saldo += valor

    def sacar_dinheiro(self, valor):
        self.saldo -= valor


conta = ContaCorrente("Lucas", "02080277693")

conta.saldo = 500
conta.consultar_saldo()

conta.depositar(600)
conta.consultar_saldo()

conta.sacar_dinheiro(250)
conta.consultar_saldo()