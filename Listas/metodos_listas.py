# método .copy()
lista = [1, "Python", [40, 30, 20]]

lista2 = lista.copy()

print(lista)
print(lista2)

print(id(lista2), id(lista))

lista2[0] = 2

print(lista2)
print(lista)

# método .extend()
linguagens = ["python", "js", "c"]
print(linguagens)

linguagens.extend(["java", "c"])
print(linguagens)