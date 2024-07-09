## Iteradores

- Iterador é um objeto que contém um número contável de valores que podem ser iterados
    - Você pode percorrer todos os valores

### Ler arquivos grandes

- Economizar memória evitando carregar todas as linhas do arquivo
- Iterar linha a linha do arquivo

```python
class FileIterator:
	def __init__(self, filename):
		self.filename = open(filename)
		
	def __iter__(self):
		return self
		
	def __next__(self):
		line = self.file.readline()
		
		if line != '':
			return line
			
		else:
			self.file.close()
			raise StopIteration
			
	for line in FileIterator(*large_file.txt):
		print(line)
```