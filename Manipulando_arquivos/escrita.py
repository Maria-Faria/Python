file = open(r"C:\Users\maria\OneDrive\Área de Trabalho\Estudo\Python\Manipulando_arquivos/teste.txt", "w")

file.write("Escrevendo dados em um novo arquivo")
file.writelines(["\n", "escrevendo", "\n", "um ", "\n", "novo ", "\n", "texto"])
file.close()