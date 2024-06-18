## Como criar conjuntos

### Criando sets

- Coleção que não possui objetos repetidos

```python
set([1, 2, 3, 1, 3, 4]) # {1, 2, 3, 4}

set("abacaxi") # {"b", "a", "c", "x", "i"}

set(("palio", "gol", "celta", "palio")) # {"gol", "celta", "palio"}
```

- Não garante a ordem

### Acessando os dados

- Não suportam indexação e nem fatiamento
- Para acessar os valores é necessário converter o conjunto para lista

```python
numeros = {1, 2, 3, 2}

numeros = list(numeros)

numeros[0]
```

### Iterar conjuntos

- Utilizando ***for***

```python
carros = {"gol", "celta", "palio"}

for carro in carros:
		print(carro)
```

### Função enumerate

- Saber qual o índice do objeto dentro do laço ***for***

```python
carros = {"gol", "celta", "palio"}

for indice, carro in enumerate(carros):
		print(f"{indice}: {carro}")
```

## Métodos da classe set

### { }.union

```python
conjunto_a = {1, 2}
conjunto_b = {3, 4}

conjunto_a.union(conjunto_b) # 1, 2, 3, 4
```

### { }.intersection

 

```python
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

conjunto_a.intersection(conjunto_b) # 2, 3
```

### { }.difference

```python
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

conjunto_a.difference(conjunto_b) # 1
conjunto_b.difference(conjunto_a) # 4
```

### { }.symmetric_difference

- Tudo que não está na intersecção

```python
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

conjunto_a.symmetric_difference(conjunto_b) # 1, 4
```

### { }.issubset

- Subconjunto

```python
conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

conjunto_a.issubset(conjunto_b) # True
conjunto_b.issubset(conjunto_a) # False
```

### { }.issuperset

```python
conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

conjunto_a.issuperset(conjunto_b) # False
conjunto_b.issuperset(conjunto_a) # True
```

### { }.isdisjoint

- Nenhum elemento em comum

```python
conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}

conjunto_a.isdisjoint(conjunto_b) # True
conjunto_a.isdisjoint(conjunto_c) # False
```

### { }.add

- Adiciona somente se o elemento não existir

```python
sorteio = {1, 23}

sorteio.add(25) # {1, 23, 25}
sorteio.add(42) # {1, 23, 25, 42}
sorteio.add(25) # {1, 23, 25, 42}
```

### { }.clear

```python
sorteio = {1, 23}

sorteio # {1, 23}
sorteio.clear()
sorteio # {}
```

### { }.copy

```python
sorteio = {1, 23}

sorteio # {1, 23}
sorteio.copy()
sorteio # {1, 23}
```

### { }.discard

- Descartar um valor

```python
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

numeros # {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
numeros.discard(1)
numeros.discard(45)
numeros # {2, 3, 4, 5, 6, 7, 8, 9, 0}
```

### { }.pop

- Remove o primeiro elemento

```python
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

numeros # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
numeros.pop() # 0
numeros.pop() # 1

numeros # {2, 3, 4, 5, 6, 7, 8, 9}
```

### { }.remove

- Diferente do *discard*, dá um erro ao tentar remover um elemento que não existe

```python
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
numeros # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

numeros.remove(0)
numeros # {1, 2, 3, 4, 5, 6, 7, 8, 9}
```

### len

```python
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

len(numeros) # 10
```

### in

```python
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

1 in numeros # True
10 in numeros # False
```
