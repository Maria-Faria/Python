def exibir_poema(data_extenso, *args, **kwargs):
		texto = "\n".join(args)
		meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
		mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
		
		print(mensagem)
		
exibir_poema(
	"Domingo, 23 de junho de 2024",
	"Zen of Python", 
	"Beautiful is better than ugly.", 
	"Explicit is better than implicit",
	"Simple is better than complex",
	"Complex is better than complicated",
	"Flat is better than nested",
	"Sparse is better than dense",
	autor="Tim Peters", 
	ano = 1999)