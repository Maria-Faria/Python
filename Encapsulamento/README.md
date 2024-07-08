## O que é encapsulamento

### Proteção de acesso

- Descreve a ideia de agrupar dados e os métodos que manipulam esses dados em uma unidade
- Impõe restrições ao acesso direto a variáveis e métodos e pode evitar a modificação acidental de dados
- A variável de um objeto só pode ser alterada pelo método desse objeto
- getters e setters

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

### Para que servem

- property( )
- Criar atributos gerenciados em classes
- Pode usar quando precisar modificar sua implementação interna sem alterar a API pública da classe

```python
class Foo:
	def __init__(self, x = None):
	self._x = x
	
	@property
	def x(self):
		return self._x or 0
		
	@x.setter
	def x(self, value):
		_x = self._x or 0
		_value = value or 0
		self._x = _x + _value
		
	@x.deleter
	def x(self):
		self._x = -1
		
	foo = Foo(10)
	print(foo.x)
	
	foo.x = 10
	print(foo.x)
	
	del foo.x
	print(foo.x)
```