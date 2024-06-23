# Funções

- Bloco de código identificado por um nome
- Pode receber uma lista de parâmetros
    - Podem ou não ter valores padrões
- Tornar o código mais legível
- Reaproveitamento de código
- Programar de maneira estruturada

```python
def exibir_mensagem():
		print('Olá, mundo!')
		
def exibir_mensagem_2(nome):
		print(f"Seja bem vindo, {nome}!")
		
def exibir_mensagem_3(nome = "Anônimo"):
		print(f"Seja bem vindo, {nome}!")
		
exibir_mensagem()
exibir_mensagem_2(nome = "Maria")
exibir_mensagem_3()
exibir_mensagem_3(nome = "Chappie")
```

## Retornando valores

- return
- Toda função Python retorna ***none*** por padrão
- Em Python uma função pode retornar mais de um valor

```python
def calcular_total(numeros):
		return sum(numeros)
		
def retorna_antecessor_sucessor(numero):
		antecessor = numero - 1
		sucessor = numero + 1
		
		return antecessor, sucessor
		
		
calcular_total([10, 20, 34]) #64
retorna_antecessor_sucessor(10) #(9, 11)
```

## Argumentos nomeados

- Funções também podem ser chamadas usando argumentos nomeados da forma chave = valor

```python
def salvar_carro(marca, modelo, ano, placa):
		print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")
		
salvar_carro("Fiat", "Palio", 1999, "ABC-1234")
salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234")
salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC-1234"})
```

## Args e kwargs

- Combinar parâmetros obrigatórios
- *args e **kwargs
- Método recebe os valores como tupla e dicionário

```python
def exibir_poema(data_extenso, *args, **kwargs):
		texto = "\n".join(args)
		meta_dados = "\n".join([f"{chave.title()}: {valor}" for cahve, valor in kwargs.items()])
		mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
		
		print(mensagem)
		
exibir_poema("Zen of Python", "Beautiful is better than ugly.", autor="Tim Peters", ano = 1999)
```

## Parâmetros especiais

- Restringir a maneira pelo qual argumentos possam ser passados

### Positional only

```python
def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
		print(modelo, ano, placa, marca, motor, combustivel)
		
# / delimita que tudo que vem antes deve ser passado pela posição APENAS
```

### Keyword only

```python
def criar_carro(*, modelo, ano, placa, marca, motor, combustivel):
		print(modelo, ano, placa, marca, motor, combustivel)
```

### Keyword an positional only

```python
def criar_carro(modelo, ano, placa, /, *, marca, motor, combustivel):
		print(modelo, ano, placa, marca, motor, combustivel)
		
criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") #válido

criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") #inválido
```

## Objetos de primeira classe

- Em Python tudo é objeto
    - Funções são objetos de primeira classe
- Podemos atribuir ***funções a variáveis, passá-las como parâmetro para funções, usá-las como valores em estruturas de dados***
    - Usar como valor de retorno para uma função (closures)

```python
def somar(a, b):
	return a + b
	
def exibir_resultado(a, b, funcao):
	resultado = funcao(a, b)
	print(f"O resultado da operação {a} + {b} = {resultado}")
	
exibir_resultado(10, 10, somar)
```

## Escopo local e escopo global

- Dentro do bloco da função o escopo é local
- Palavra-chave ***global***
    - ***Não é uma boa prática e deve ser evitada***

```python
salario = 2000 # escopo global

def salario_bonus(bonus):
		global salario
		salario += bonus
		
		return salario
		
salario_bonus(500) # 2500
```