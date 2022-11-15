"""
3. Crie uma classe representando os alunos de um determinado curso. A classe deve
conter os atributos matrícula do aluno, nome, nota da primeira prova, nota da segunda
prova e nota da terceira prova. Crie metodos para acessar o nome e a média do aluno. 
(a) Permita ao usuario entrar com os dados de 5 alunos. 
(b) Encontre o aluno com maior media geral. 
(c) Encontre o aluno com menor media geral 
(d) Para cada aluno diga se ele foi aprovado ou reprovado, considerando o valor 6 para
aprovação. 
"""

class Alunos:
    
    def __init__(self, matricula, nome, nota1, nota2, nota3):
        self.matricula = matricula
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        
    def mostrar_nome(self):
        return self.nome
        
    def mostrar_media(self):
        media = (self.nota1 + self.nota2 + self.nota3) / 3
        return media
        
        
#inicio - programa
aluno1 = Alunos("123", "Lucas", 9, 8, 10)
aluno2 = Alunos("456", "Maria", 9, 4, 7)
aluno3 = Alunos("789", "Luan", 2, 9, 6)
aluno4 = Alunos("321", "Dilton", 7, 8, 3)
aluno5 = Alunos("654", "Nair", 4, 3, 9)

media_alunos = []

media_alunos.append((aluno1.mostrar_media(), aluno1.mostrar_nome()))
media_alunos.append((aluno2.mostrar_media(), aluno2.mostrar_nome()))
media_alunos.append((aluno3.mostrar_media(), aluno3.mostrar_nome()))
media_alunos.append((aluno4.mostrar_media(), aluno4.mostrar_nome()))
media_alunos.append((aluno5.mostrar_media(), aluno5.mostrar_nome()))

maior = 0
menor = 0
for media in media_alunos:
    if maior == 0 and menor == 0:
        maior = media[0]
        nome_maior = media[1]
        menor = media[0]
        nome_menor = media[1]
    else:
        if media[0] > maior:
            maior = media[0]
            nome_maior = media[1]
        elif media[0] < menor:
            menor = media[0]
            nome_menor = media[1]
            
    if media[0] >= 6:
        print(f"O aluno {media[1]} foi aprovado")
    else:
        print(f"O aluno {media[1]} foi reprovado")
            
print("-" * 30)            
print(f"O aluno com maior média geral foi {nome_maior} com {maior:.2f} porntos.\n"
      f"O aluno com menor média foi {nome_menor} com {menor:.2f} pontos.")


    

