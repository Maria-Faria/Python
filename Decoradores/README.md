## Decoradores

- Funções em Python são objetos de primeira classe
    - ***Podem ser passadas e usadas como argumentos***

```python
def dizer_oi(nome):
	return f"Oi, {nome}"
	
def incentivar_aprender(nome):
	return f"Oi, {nome}, vamos aprender Python juntos!"
	
def mensagem_para_guilherme(funcao_mensagem):
	return funcao_mensagem("Guilherme")
	
mensagem_para_guilherme(dizer_oi)
mensagem_para_guilherme(incentivar_aprender)
```

### Inner functions

- Funções definidas dentro de outras funções
- Funções internas

```python
def pai():
	print("Escrevendo da pai()")
	
	def filho1():
		print("Escrevendo da filho1()")
		
	def filho2():
		print("Escrevendo da filho2()")
		
	filho2()
	filho1()
	
pai()

#Escrevendo da pai()
#Escrevendo da filho2()
#Escrevendo da filho1()
```

### Retornando funções de funções

- Python permite que você use funções como valores de retorno

```python
def calcular(operacao):
	def somar(a, b):
		return a + b
		
	def subtrair(a, b):
		return a - b
		
	if operacao == "+":
		return somar
		
	else:
		return subtrair
		
resultado = calcular("+")(1, 3)
```

### Decorador simples

```python
def meu_decorador(funcao):
	def envelope():
		print("Faz algo antes de executar a função")
		funcao()
		print("Faz algo depois de executar a função")
		
	return envelope
	
def ola_mundo():
	print("Olá mundo")
	
ola_mundo = meu_decorador(ola_mundo)
ola_mundo()
```

### Açúcar sintático

- O Python permite que você ***use decoradores de maneira mais simples com o @***

```python
def meu_decorador(funcao):
	def envelope():
		print("Faz algo antes de executar a função")
		funcao()
		print("Faz algo depois de executar a função")
		
	return envelope
	
@meu_decorador
def ola_mundo():
	print("Olá mundo")
	
ola_mundo()
```

### Funções de decoração com argumentos

- Podemos usar ****args e **kwargs*** na função interna
    - Aceitará um número arbitrário de argumentos posicionais e de palavras-chave

```python
def duplicar(func):
	def envelope(*args, **kwargs):
		func(*args, **kwargs)
		func(*args, **kwargs)
		
	return envelope
	
@duplicar
def aprender(tecnologia):
	print(f"Estou aprendendo {tecnologia}")
	
aprender("Python")
```

### Retornando valores de funções decoradas

- O decorador pode decidir se retorna o valor da função decorada ou não
- Para que o valor seja retornado a função de ***envelope*** deve retornar o valor da função decorada

```python
def duplicar(func):
	def envelope(*args, **kwargs):
		func(*args, **kwargs)
		return func(*args, **kwargs)
		
	return envelope
	
@duplicar
def aprender(tecnologia):
	print(f"Estou aprendendo {tecnologia}")
	return tecnologia.upper()
	
tecnologia = aprender("Python")
print(tecnologia)
```

### Introspecção

- Capacidade de um objeto saber sobre seus próprios atributos em tempo de execução

```python
import functools

def duplicar(func):
	@functools.wraps(func)
	def envelope(*args, **kwargs):
		func(*args, **kwargs)
		return func(*args, **kwargs)
		
	return envelope
	
@duplicar
def aprender(tecnologia):
	print(f"Estou aprendendo {tecnologia}")
	return tecnologia.upper()
	
tecnologia = aprender("Python")
print(tecnologia)
```
