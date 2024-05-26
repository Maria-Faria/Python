name = "Maria"
age = 20
profession = "Programadora"
language = "Python"
balance = 45.435

data = {"name": "Maria", "age": 20}

# usando porcentagem
print("Nome: %s Idade: %d" % (name, age))

# método Format
print("Nome: {} Idade: {}".format(name, age))
print("Nome: {1} Idade: {0}".format(age, name))
print("Nome: {1} Idade: {0} Nome: {1}".format(age, name))
print("Nome: {name} Idade: {age}".format(age=age, name=name))
print("Nome: {name} Idade: {age}".format(**data)) # usando um dicionário

# f-string
print(f"Nome: {name} Idade: {age}")
print(f"Nome: {name} Idade: {age} Saldo: {balance:.2f}") # argumento antes do ponto --> espaço antes do número