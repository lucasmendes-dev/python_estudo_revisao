"""
4. Crie uma classe para representar um numero complexo. Implemente, usando sobrecarga 
de operador, os metodos para fazer as operações de soma, subtração e produto entre 
dois numeros
"""

class Numero:
    
    def __init__(self, numero):
        self.numero = numero
        
    def soma(self, num):
        return self.numero + num
    
    def subtracao(self, num):
        return self.numero - num
    
    def multiplicacao(self, num):
        return self.numero * num
    
    
numero = Numero(10.9)

print(numero.soma(9))
print(numero.multiplicacao(19.8))
print(numero.subtracao(6.54))



