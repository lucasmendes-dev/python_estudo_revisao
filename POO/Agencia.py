from random import randint

class Agencia:
    
    def __init__(self, telefone, cnpj, numero):
        self.telefone = telefone
        self.cnpj = cnpj
        self.numero = numero
        self.clientes = []
        self.caixa = 0
        self.emprestimos = []
        
    def verificar_caixa(self):
        if self.caixa < 1000000:
            print(f"Caixa abaixo do nível recomendado. Caixa atual: {self.caixa}")
        else:
            print(f"O valor de caixa está ok. Caixa atual: {self.caixa}")
            
    def emprestar_dinheiro(self, valor, cpf, juros):
        if self.caixa > valor:
            self.emprestimos.append((valor, cpf, juros))
        else:
            print("Empréstimo não é possível. Dinheiro não disponível em caixa.")
        
    def adicionar_cliente(self, nome, cpf, patrimonio):
        self.clientes.append((nome, cpf, patrimonio))
        
    
class AgenciaVirtual(Agencia):   #sintaxe do extends: like "AgenciaVirtual extends Agencia"
    
    def __init__(self, site, telefone, cnpj):
        self.site = site
        super().__init__(telefone, cnpj, 1000)  #usando o método init da classe mãe(super classe)
        self.caixa = 1000000
        self.caixa_paypal = 0
        
    def depositar_paypal(self, valor):
        self.caixa -= valor
        self.caixa_paypal += valor
    
    def sacar_paypal(self, valor):
        self.caixa_paypal -= valor
        self.caixa += valor
        
    
class AgenciaComum(Agencia):
    
    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, numero= randint(1001, 9999))
        self.caixa = 1000000
        
        
class AgenciaPremium(Agencia):
    
    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, numero= randint(1001, 9999))
        self.caixa = 2000000   
        
    def adicionar_cliente(self, nome, cpf, patrimonio): #ideia de "Polimorfismo", alterando método apenas na classe filha
        if patrimonio > 1000000:
            super().adicionar_cliente(nome, cpf, patrimonio)
        else:
            print("O clinte não tem o patrimônio mínimo necessário para entrar na agência premium")
        

if __name__ == "__main__":   #se arquivo estiver sendo importado no "main" este trecho não será executado
    
    agencia1 = Agencia("(31)99246-7832", 123456789, 3610)

    agencia_virtual = AgenciaVirtual("www.agenciavirtual.com.br", "(31)98302-6013", 9876543212)
    agencia_virtual.verificar_caixa()
    print(agencia_virtual.site)

    agencia_comum = AgenciaComum("(31)98302-6013", 123456789)
    print(agencia_comum.numero)

    agencia_premium = AgenciaPremium("(31)92584-7412", 654659875)
    agencia_premium.verificar_caixa()

    agencia_virtual.depositar_paypal(20000)
    print(agencia_virtual.caixa)
    print(agencia_virtual.caixa_paypal)

    agencia_premium.adicionar_cliente("Maria", 12345678912, 1500000)
    print(agencia_premium.clientes)