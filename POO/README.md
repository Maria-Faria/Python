## O que é Orientação a Objetos

### Paradigmas de programação

- Estilo de programação
- Não é uma linguagem, e sim a forma como você soluciona os problemas através do código
- ***Exemplo***
    - Problema: beber água
    - Solução 1: usar um copo para beber água
    - Solução 2: usar uma garrafa para beber água
- ***Alguns paradigmas***
    - Imperativo ou procedural
    - Funcional
    - Orientado a eventos

### Programação orientada a objetos

- Estrutura o código abstraindo problemas em objetos do mundo real, facilitando o entendimento do código e tornando-o mais modular e extensível
- Classes e objetos

## Classes e Objetos

### Conceito de classes e objetos

- ***Classe***
    - Define as características e comportamentos de um objeto
    - Não conseguimos usá-las diretamente
    
    ```python
    class Cachorro:
    		def __init__(self, nome, cor, acordado = True):
    				self.nome = nome
    				self.cor = cor
    				self.acordado = acordado
    				
    		def latir(self):
    				print("Auau")
    				
    		def dormir(self):
    				self.acordado = False
    				print("Zzzzz...")
    ```
    
- ***Objeto***
    - Podemos usá-los
    - Possuem as características e comportamentos que foram definidos nas classes
    
    ```python
    cao_1 = Cachorro("chappie", "amarelo", False)
    cao_2 = Cachorro("Aladim", "branco e preto")
    
    cao_1.latir()
    
    print(cao_2.acordado)
    cao_2.dormir()
    print(cao_2.acordado)
    ```
    

### Primeiro programa em POO

- João tem uma bicicletaria e gostaria de registrar as vendas de suas bicicletas. Crie um programa onde João informe: ***cor, modelo, ano e valor*** da bicicleta vendida. Uma bicicleta pode: ***buzinar, parar e correr***. Adicione esses comportamentos!
- ***Self***
    - Referência ao objeto
    - O mesmo que *this*
- Métodos são funções que estão dentro de uma classe
    - Precisam do ***self*** como primeiro argumento

## Construtores e destrutores

### Método construtor

- Sempre é executado quando uma nova instância da classe é criada
- Inicializamos o estado do nosso objeto
- __init__

```python
class Cachorro:
		def __init__(self, nome, cor, acordado=True):
				self.nome = nome
```

### Método destrutor

- Executado sempre que uma instância é destruída
- Python tem um coletor de lixo
- __del__

```python
class Cachorro:
		def __del__(self):
				print("destrunindo a instância")
```