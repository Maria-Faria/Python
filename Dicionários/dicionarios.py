contatos = {
    "maria@gmail.com": {"nome": "Maria", "telefone": "00 1234-3542"},
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "melanie@gmail.com": {"nome": "Melanie", "telefone": "3333-7766", "extra": {"a": 1}}
}

telefone = contatos["giovanna@gmail.com"]["telefone"]
print(telefone)

extra = contatos["melanie@gmail.com"]["extra"]["a"]
print(extra)

# iterar dicionários
for chave in contatos:
    print(chave, contatos[chave])

print('-----------------------')

for chave, valor in contatos.items():
    print(chave, valor)

# MÉTODO GET
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
}

#print(contatos["chave"]) -> KeyError
print(contatos.get("chave"))