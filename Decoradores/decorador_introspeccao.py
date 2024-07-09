import functools

def meu_decorador(funcao):
    @functools.wraps(funcao)
    def envelope(*args, **kwargs):
        print("Faz algo antes de executa a função")
        resultado = funcao(*args, **kwargs)
        print("Faz algo depois de executar a função")
        return resultado
    return envelope

@meu_decorador
def ola_mundo(nome):
    print(f"Olá mundo {nome}")
    return nome.upper()

print(ola_mundo.__name__)