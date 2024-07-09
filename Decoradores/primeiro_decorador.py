def meu_decorador(funcao):
    def envelope():
        print("Faz algo antes de executa a função")
        funcao()
        print("Faz algo depois de executar a função")

    return envelope

def ola_mundo():
    print("Olá mundo")

ola_mundo = meu_decorador(ola_mundo) #atribuir novo valor à função 
ola_mundo()