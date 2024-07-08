## Variáveis de classe e variáveis de instância

### Atributos do objeto

- Todos os objetos nascem com o mesmo número de atributos de classe e de instância
- Atributos de instância → diferentes par cada objeto
- Atributos de classe → compartilhados entre os objetos

```python
class Estudante:
	escola = "DIO"
	
	def __init__(self, nome, numero):
		self.nome = nome
		self.numero = numero
		
	def __str__(self):
		return f"{self.nome} ({self.numero}) - {self.escola}"
```

## Métodos de classe e métodos estáticos

### Métodos de classe

- Ligados à classe e não ao objeto
- Têm acesso ao estado da classe
    - Recebem um parâmetro que aponta para a classe e não para a instância do objeto

### Métodos estáticos

- Não recebe um primeiro argumento explícito
- Também é vinculado à classe e não ao objeto
- Não pode acessar ou modificar o estado da classe
- Está presente em uma classe porque faz sentido que o método esteja presente na classe

### Quando utilizar método de classe ou estático

- Método de classe → criar métodos de fábrica
- Métodos estáticos → criar funções utilitárias

## O que são interfaces

- Interfaces definem o que uma classe ***deve fazer*** e não como
- Definir um contrato
- Classes abstratas em Python
    - Não podem ser instanciadas

## Classes abstratas

### ABC

- Abstract Base Class
- Módulo que fornece a base para definir as classes abstratas
- Decora métodos da classe base como abstratos e em seguida registra classes concretas como implementações da base abstrata
- Um método se torna abstrato quando decorado com ***@abstractmethod***