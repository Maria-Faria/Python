class Cachorro:
    def __init__(self, nome, cor, acordado = True):
        print("Inicializando a classe...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self):
        print("Removendo a instância da classe")

    def latir(self):
        print("Auau")

def criar_cachorro():
    c = Cachorro("Zeus", "Branco e preto", False)
    print(c.nome)

c1 = Cachorro("Kiara", "cinza")
c1.latir()

print("Olá")

del c1
print("Olá")
print("Olá")
print("Olá")
print("Olá")


#criar_cachorro()

