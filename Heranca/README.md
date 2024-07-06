## Herança em POO

- Herança é a capacidade de uma classe filha derivar ou herdar as características e comportamentos da classe pai (base)

### Benefícios

- Representa bem os relacionamentos do mundo real
- Reutilização de código
    - Permite adicionar mais recursos a uma classe sem modificá-la
- Natureza transitiva
    - Se a classe B herdar da classe A, todas as subclasses de B herdarão automaticamente da classe A

```python
class A:
		pass
		
class B(A):
		pass
```

## Herança simples e herança múltipla

### Herança simples

- Quando uma classe filha herda apenas de uma classe pai

### Herança múltipla

- Quando uma classe filha herda de várias classes pai

```python
class A:
		pass
		
class B:
		pass
		
class C(A, B):
		pass
```