from datetime import datetime
import pytz


class ContaCorrente:

    @staticmethod
    def _data_hora():   #método "estático", não precisa ter self e fica acima do __init__
        fuso_BR = pytz.timezone("Brazil/East")
        horario_BR = datetime.now(fuso_BR)
        return horario_BR.strftime('%d/%m/%Y %H:%M:%S') #formatação de horário

    def __init__(self, nome, cpf, agencia, num_conta):
        self._nome = nome
        self._cpf = cpf
        self._saldo = 0
        self._limite = None
        self._agencia = agencia
        self._num_conta = num_conta
        self._transacoes = []

    def consultar_saldo(self):
        print(f"Seu saldo atual é de R${self._saldo:.2f}")

    def depositar(self, valor):
        self._saldo += valor
        self._transacoes.append((valor, self._saldo, ContaCorrente._data_hora()))
        
    def _limite_conta(self):     #o uso da "_" antes do nome é uma convenção para a função ser privada
        self._limite = -1000
        return self._limite

    def sacar_dinheiro(self, valor):
        if self._saldo - valor < self._limite_conta():
            print("Você não tem saldo suficiente para sacar esse valor.")
            self.consultar_saldo()
        else:
            self._saldo -= valor
            self._transacoes.append((-valor, self._saldo, ContaCorrente._data_hora()))

    def consultar_limite_chequeEspecial(self):
        print(f"Seu limite de Cheque Especial é de R${self._limite_conta():.2f}")
        
    def consultar_historico_transacoes(self):
        print("Histórico de Transações:")
        for transacao in self._transacoes:
            print(transacao)
            
    def transferir(self, valor, conta_destino):
        self._saldo -= valor
        self._transacoes.append((-valor, self._saldo, ContaCorrente._data_hora()))
        conta_destino.saldo += valor
        conta_destino._transacoes.append((-valor, conta_destino.saldo, ContaCorrente._data_hora()))
        

conta = ContaCorrente("Lucas", "02080277693", 3610, 33794)

conta.saldo = 500
conta.consultar_saldo()

conta.depositar(600)
conta.consultar_saldo()


print("Saldo final")
conta.consultar_limite_chequeEspecial()

print("-" * 20)
conta.consultar_historico_transacoes()

print("-" * 20)
conta_2 = ContaCorrente("Maria", "12345678900", 1234, 66584)
conta.transferir(240, conta_2)

conta.consultar_saldo()
conta_2.consultar_saldo()