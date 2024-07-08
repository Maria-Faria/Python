from abc import ABC, abstractmethod, abstractproperty

class ControleRemoto(ABC):

    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @property
    @abstractproperty
    def marca(self):
        pass

class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando a TV...")
        print("TV ligada!")

    def desligar(self):
        print("Desligando a TV...")
        print("TV desligada!")

    @property
    def marca(self):
        return "Philco"

class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("Ligando o Ar condicionado...")
        print("Ar condicionado ligado!")

    def desligar(self):
        print("Desligando ar condicionado...")
        print("Ar condicionado desligado!")

    @property
    def marca(self):
        return "LG"

controle = ControleTV()
controle.ligar()
controle.desligar()
print(controle.marca)

controle = ControleArCondicionado()
controle.ligar()
controle.desligar()
print(controle.marca)

