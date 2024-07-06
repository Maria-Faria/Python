class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("Ligando o motor...")

    def __str__(self):
        return self.cor
class Motocicleta(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado

    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'}")

class Carro(Veiculo):
    pass

moto = Motocicleta("Azul", "ABC-1234", 2)
moto.ligar_motor()
print("**************************")

carro = Carro("Branco", "XDE-0098", 4)
carro.ligar_motor()
print("**************************")

caminhao = Caminhao("Roxo", "GFD-8712", 8, True)
caminhao.ligar_motor()
caminhao.esta_carregado()