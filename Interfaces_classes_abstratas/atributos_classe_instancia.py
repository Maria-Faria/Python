class Estudante:
    escola = "DIO" #atributo de classe

    def __init__(self, nome, numero):
        self.nome = nome #atributo de instância
        self.numero = numero

    def __str__(self):
        return f"{self.nome} - {self.numero} - {self.escola}"
    
def mostrar_valores(*objs):
    for obj in objs:
        print(obj)

aluno1 = Estudante("Maria Eduarda", "CG3023141")
aluno2 = Estudante("Guilherme", "CG342654X")
mostrar_valores(aluno1, aluno2)

Estudante.escola = "Python"

aluno3 = Estudante("José", "CG5214578")

mostrar_valores(aluno1, aluno2, aluno3)
