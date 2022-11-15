"""
5. Classe Quadrado: Crie uma classe que modele um quadrado:

Atributos: Tamanho do lado
Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;
"""

class Quadrado:
    
    def __init__(self, tamanho_lado):
        self.tamanho_lado = tamanho_lado
        
    def set_tamanho_lado(self, valor):
        self.tamanho_lado = valor 

    def get_tamanho_lado(self):
        return self.tamanho_lado
        
    def calcular_area(self):
        return self.tamanho_lado * self.tamanho_lado
    

objeto = Quadrado(5)
print(objeto.get_tamanho_lado())

objeto.set_tamanho_lado(8)
print(objeto.get_tamanho_lado())

print(objeto.calcular_area())