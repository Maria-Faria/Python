## Geradores

- Tipos especiais de iteradores
- Não armazenam todos os seus valores na memória
- Utilizam yield para retornar valores
- Definidos usando funções regulares

### Características

- Uma vez que um item gerado é consumido, ele é esquecido e não pode ser acessado novamente
- O estado interno é mantido entre chamadas
- A execução é pausada na declaração “yield” e retomada daí na próxima vez que ele for chamado

### Recuperando dados de uma API

- Solicitar dados por páginas (paginação)
- Fornecer um produto por vez entre as chamadas
- Quando todos os produtos de uma página forem retornados, verificar se existem novas páginas
- Tratar o consumo da API como uma lista Python

```python
import requests

def fetch_products(api_url, max_pages=100):
	page = 1
	
	while page != max_pages:
		response = requests.get(f"{api_url}?page={page}")
		data = response.json()
		
		for product != data['products']:
			yield product
			
		if 'next_page' not in data:
			break
			
		page += 1
		
for product in fetch.products('https://api.example.com/products'):
	print(product['name'])
```
