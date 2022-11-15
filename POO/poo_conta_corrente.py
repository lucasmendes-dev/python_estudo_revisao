from datetime import datetime
import pytz
from random import randint   


class ContaCorrente:

    """_summary_
        Cria um objeto ContaCorrente para gerenciar as contas dos clientes.
        
    Atributos:
        nome (str): Nome do cliente.
        cpf (str): Cpf do cliente.
        saldo (int): Saldo disponível na conta do cliente.
        limite (int): Limite de Cheque Especial daquele cliente.
        agencia(int): Agência responsável pela conta do cliente.
        num_conta (int): Número da conta corrente do cliente.
        transacoes (arr): Histórico de transacoes do cliente.
        cartoes (arr): Armazena os cartões de crédito do cliente.
    """

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
        self.agencia = agencia
        self.num_conta = num_conta
        self._transacoes = []
        self.cartoes = []

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
    
    
class CartaoCredito:
    
    @staticmethod
    def _data_hora():   
        fuso_BR = pytz.timezone("Brazil/East") 
        horario_BR = datetime.now(fuso_BR)
        return horario_BR
    
    def __init__(self, titular, conta_corrente):
        self.numero = randint(1000000000000000, 9999999999999999)
        self.titular = titular
        self.validade = "{}/{}".format(CartaoCredito._data_hora().month, CartaoCredito._data_hora().year + 4)  #formatando data e ano
        self.cod_seguranca = "{}{}{}".format(randint(0, 9), randint(0, 9), randint(0, 9))
        self.limite = 1000
        self._senha = "1234"
        self.conta_corrente = conta_corrente
        conta_corrente.cartoes.append(self)    #adiciona a classe CartaoCredito no atributo "_cartoes" da classe ContaCorrente

    @property   #transforma a função em um atributo
    def senha(self):
        return self._senha
    
    @senha.setter   #definir a senha
    def senha(self, valor):
        if len(valor) == 4 and valor.isnumeric():
            self._senha = valor
        else:
            print("Nova senha inválida")
    

#início - programa
conta = ContaCorrente("Lucas", "02080277693", 3610, 33794)
cartao = CartaoCredito("Lucas", conta)

#print(conta.cartoes[0].numero)  #forma de exibir um objeto dentro de outro

cartao.senha = "12"    #não precisa mais do "_" para exibir ou alterar, pelo fato de usar o @property e @.setter
print(cartao.senha)

print(conta.__dict__) #__dict__ serve para consultar os valores inseridos na classe
