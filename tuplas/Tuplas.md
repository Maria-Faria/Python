## Criação e acesso aos dados

### Criando tuplas

- Irmã da lista
- Imutáveis
- Classe ***tuple***
- Colocar valores separados por vírgula de parênteses

```python
frutas = ("laranja", "pera", "uva",)

letras = tuple("python")

numeros = tuple([1, 2, 3, 4])

pais = ("Brasil",)
```

### Acesso direto

- Tupla é uma sequência
- Acessamos utilizando índices
    - A partir do zero

```python
frutas = ("maçã", "laranja", "uva", "pera",)

frutas[0] # maçã

frutas[-1] # pera
frutas[-3] # laranja
```

### Tuplas aninhadas

- Tuplas podem armazenar todos os tipos de objetos Python
    - Podemos ter tuplas que armazenam outras tuplas
- Estruturas bidimensionais (tabelas)
    - Acessar informando linha e coluna

```python
matriz = (
	(1, "a", 2),
	("b", 3, 4),
	(6, 5, "c"),
)

matriz[0] #(1, "a", 2)
matriz[0][0] # 1
```

### Fatiamento

- Extrair um conjunto de valores
- Passar o índice inicial e/ou final
- Podemos informar quantas posições o cursor deve pular no acesso

```python
tupla = ("p", "y", "t", "h", "o", "n")

tupla(2:) # (t, h, o, n)
tupla(:2) # (p, y)
tupla(1:3) # (y, t)
tupla(0:3:2) # (p, t)
tupla(::) # (p, y, t, h, o, n)
tupla(::-1) # (n, o, h, t, y, p)
```

### Iterar tuplas

- Utilizando ***for***

```python
carros = ("gol", "celta", "palio",)

for carro in carros:
	print(carro)
	
	
for indice, carro in enumerate(carros):
	print(f"{indice}: {carro}")
```

## Métodos da classe tuple

### ( ).count

```python
cores = ("vermelho", "azul", "verde", "azul",)

cores.count("vermelho") # 1
cores.count("azul") # 2
cores.count("verde") # 1
```

### ( ).index

```python
linguagens = ("python", "js", "c", "java", "csharp",)

linguagens.index("java") # 3
linguagens.index("python") # 0
```

### len
