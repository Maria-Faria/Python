name = "MaRia"

#Maiúsculas
print(name.upper())

#Minúsculas
print(name.lower())

#Título
print(name.title())

text = "   Hello World!   "

print(text + ".")

# removendo espaços em branco
print(text.strip() + ".")

# removendo espaços da esquerda
print(text.lstrip() + ".")

# removendo espaços da direita
print(text.rstrip() + ".")

menu = "Python"

print("####" + menu + "####")

# centralizando
print(menu.center(14)) # quantidade de caracteres

print(menu.center(14, "#"))

# juntando
print("P-y-t-h-o-n")

print("-".join(menu))