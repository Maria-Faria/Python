class Pessoa:
    def __init__(self, nome = None, idade = None):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_a_partir_data_nascimento(cls, ano, mes, dia, nome):
        print(cls)
        idade = 2024 - ano
        return cls(nome, idade) #cls é a referência p/ classe
    
    @staticmethod
    def e_maior_idade(idade):
        return idade > 17

p =Pessoa("Maria Eduarda", 20)
print(p.nome, p.idade)

p2 = Pessoa.criar_a_partir_data_nascimento(2004, 3, 15, "Maria")
print(p2.nome, p2.idade)

print(Pessoa.e_maior_idade(17))
