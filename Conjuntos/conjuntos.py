# CRIANDO SETS
numeros = set([1, 2, 3, 1, 3, 4])
print(numeros)

letras = set("abacaxi")
print(letras)

carros = set(("palio", "gol", "celta", "palio"))
print(carros)

linguagens = {"python", "java", "python"}
print(linguagens)

# ACESSANDO DADOS
numeros = {1, 2, 3, 2}
numeros = list(numeros)

print(numeros[0])

#MÉTODO POP
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
print(numeros)

print(numeros.pop())
print(numeros.pop())

print(numeros)

#MÉTODO REMOVE
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
print(numeros)

numeros.remove(0)
print(numeros)