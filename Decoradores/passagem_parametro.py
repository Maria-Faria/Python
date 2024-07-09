def message(name):
    print("Executando nome")
    return f"Oi, {name}"

def long_message(name):
    print("Executando mensagem longa")
    return f"Olá, tudo bem com você, {name}?"

def execute(function, name):
    print("Executando executar")
    return function(name)

print(execute(message, "Maria"))
print(execute(long_message, "Maria"))