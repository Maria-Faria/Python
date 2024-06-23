salario = 2000 # escopo global

def salario_bonus(bonus, lista):
    global salario
    salario += bonus

    lista.append(2)
    
    return salario
		
lista = [1]
print(salario_bonus(500, lista)) # 2500

print(lista)