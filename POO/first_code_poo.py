class Bike:
    #construtor
    def __init__(self, color, model, year, value):
        self.color = color,
        self.model = model,
        self.year = year,
        self.value = value

    def honk(self):
        print("Bibi")

    def stop(self):
        print("Bicicleta parou")

    def run(self):
        print("Zoooooom")