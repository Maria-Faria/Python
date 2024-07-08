## O que é polimorfismo

### Muitas formas

- Mesmo nome de função (mas assinaturas diferentes) sendo usado para tipos diferentes
- Se comporta de modos diferentes dependendo do tipo de dado inserido

```python
len("python")
len([10, 20, 30])
```

## Polimorfismo com herança

### Mesmo método com comportamento diferente

- Na herança, a classe filha herda os métodos da classe pai
- É possível modificar um método em uma classe filha herdada da classe pai

```python
class Passaro:
	def voar(self):
		pass
		
class Pardal(Passaro):
	def voar(self):
		print("Pardal voa")
		
class Avestruz(Passaro):
	def voar(self):
		print("Avestruz não voa")
		
def plano_de_voo(passaro):
	passaro.voar()
	
plano_de_voo(Pardal())
plano_de_voo(Avestruz())
```