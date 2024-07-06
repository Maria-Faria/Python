class Bike:
    # construtor
    def __init__(self, color, model, year, value):
        # atributos da classe
        self.color = color
        self.model = model
        self.year = year
        self.value = value

    def honk(self):
        print("Trim trim trim")

    def stop(self):
        print("Parandoooo")
        print("Bicicleta parou")

    def run(self):
        print("Zoooooom")

    #def __str__(self):
     #   return f"""Bike: 
      #      Cor = {self.color}, 
       #     Modelo = {self.model}, 
        #    Ano = {self.year}, 
         #   Valor = R${self.value:.2f}"""

    def __str__(self):
        return f"{self.__class__.__name__}: \n{'\n'.join([f"{key} = {value}" for key, value in self.__dict__.items()])}"

# instanciando a bike
b1 = Bike("Vermelha", "Caloi", 2022, 600)
b1.honk()
b1.run()
b1.stop()
print(b1.color, b1.model, b1.year, b1.value)

b2 = Bike("Verde", "Monark", 2000, 189)
Bike.honk(b2)
print(b2.color)
print(b2)