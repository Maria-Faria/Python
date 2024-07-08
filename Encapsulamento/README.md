## O que é encapsulamento

### Proteção de acesso

- Descreve a ideia de agrupar dados e os métodos que manipulam esses dados em uma unidade
- Impõe restrições ao acesso direto a variáveis e métodos e pode evitar a modificação acidental de dados
- A variável de um objeto só pode ser alterada pelo método desse objeto
- getters e setters

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/48347520-d389-4c9f-8b1c-fc7878f42221/5dc9104e-dd27-4503-8533-cfe2dde995aa/Untitled.png)

## Recursos públicos e privados

### Modificadores de acesso

- Em Python não temos palavras reservadas para definir o nível de acesso aos atributos
    - Usamos convenções no nome de recurso para definir se a variável é pública ou privada

### Definição

- ***Público*** → pode ser acessado de fora da classe
- ***Privado*** → só pode ser acessado pela classe
    - underline
    - Métodos dentro da classe

### Público/privado

- Todos os recursos são públicos, a menos que o nome inicie com underline
- Interpretador Python não vai garantir a proteção do recurso

```python
class Conta:
	def __init__(self, saldo = 0):
		self._saldo = saldo
		
	def depositar(self, valor):
		pass
```

## Properties