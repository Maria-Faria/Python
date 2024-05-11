"""
while True:
    numero = int(input("Informe um número: "))

    if numero == 10:
        break

    print(numero)
"""

for numero in range(0, 99):
    if numero % 2 == 0:
        continue # pula a execução e vai para o próximo

    print(numero)