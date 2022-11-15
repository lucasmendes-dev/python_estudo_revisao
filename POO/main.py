import ContaCorrente as cc
import Agencia as ag

conta = cc.ContaCorrente("Lucas", "02080277693", 3610, 33794)
cartao = cc.CartaoCredito("Lucas", conta)

#print(conta.cartoes[0].numero)  #forma de exibir um objeto dentro de outro

cartao.senha = "12"    #não precisa mais do "_" para exibir ou alterar, pelo fato de usar o @property e @.setter
print(cartao.senha)

print(conta.__dict__) #__dict__ serve para consultar os valores inseridos na classe

agencia_premium = ag.AgenciaPremium("(31)99246-7832", 12345678978)
print(agencia_premium.clientes)