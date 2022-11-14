from datetime import datetime
import pytz


class ContaCorrente:

    @staticmethod
    def _data_hora():   #método "estático", não precisa ter self e fica acima do __init__
        fuso_BR = pytz.timezone("Brazil/East")
        horario_BR = datetime.now(fuso_BR)
        return horario_BR.strftime('%d/%m/%Y %H:%M:%S') #formatação de horário

    def __init__(self, nome, cpf, agencia, num_conta):
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0
        self.limite = None
        self.agencia = agencia
        self.num_conta = num_conta
        self.transacoes = []

    def consultar_saldo(self):
        print(f"Seu saldo atual é de R${self.saldo:.2f}")

    def depositar(self, valor):
        self.saldo += valor
        self.transacoes.append((valor, self.saldo, ContaCorrente._data_hora()))
        
    def _limite_conta(self):     #o uso da "_" antes do nome é uma convenção para a função ser privada
        self.limite = -1000
        return self.limite

    def sacar_dinheiro(self, valor):
        if self.saldo - valor < self._limite_conta():
            print("Você não tem saldo suficiente para sacar esse valor.")
            self.consultar_saldo()
        else:
            self.saldo -= valor
            self.transacoes.append((-valor, self.saldo, ContaCorrente._data_hora()))

    def consultar_limite_chequeEspecial(self):
        print(f"Seu limite de Cheque Especial é de R${self._limite_conta():.2f}")
        
    def consultar_historico_transacoes(self):
        print("Histórico de Transações:")
        for transacao in self.transacoes:
            print(transacao)
        

conta = ContaCorrente("Lucas", "02080277693", 3610, 33794)

conta.saldo = 500
conta.consultar_saldo()

conta.depositar(600)
conta.consultar_saldo()

conta.sacar_dinheiro(2100)

print("Saldo final")
conta.consultar_limite_chequeEspecial()

print("-" * 20)
conta.consultar_historico_transacoes()