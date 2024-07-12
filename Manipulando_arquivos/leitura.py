arquivo = open(r"C:\Users\maria\OneDrive\Área de Trabalho\Estudo\Python\Manipulando_arquivos\lorem.txt", "r")

#print(arquivo.read())
#print(arquivo.readline()) #traz uma linha por vez
#print(arquivo.readlines()) #retorna um array

while len(linha := arquivo.readline()):
    print(linha)

arquivo.close()