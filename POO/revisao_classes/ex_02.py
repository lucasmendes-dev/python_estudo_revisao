"""
2. Crie uma classe que modele um aluno
(a) Atributos: nome, numero de matrícula e curso
(b) Metodos: mostrar curso e alterar curso 
"""

class Aluno:
    
    def __init__(self, nome, matricula, curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
        
    def mostrar_curso(self):
        print(self.curso)
    
    def alterar_curso(self, novo_curso):
        self.curso = novo_curso
    
    
lucas = Aluno("Lucas", "2016081036", "Música")

lucas.mostrar_curso()

lucas.alterar_curso("Análise e Desenvolvimento de Sistemas")

lucas.mostrar_curso()