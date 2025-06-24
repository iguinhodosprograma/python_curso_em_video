def aumentar(valor=0, taxa=0, format=False, moeda="R$"):
    aumentar = (valor * (taxa/100)) + valor
    
    if format:
        return f"{moeda}{aumentar:.2f}".replace(".", ",")
    else:
        return aumentar


def diminuir(valor=0, taxa=0, format=False, moeda="R$"):
    diminuicao = valor - (valor * (taxa/100))
    if format:
        return f"{moeda}{diminuicao:.2f}".replace(".", ",")
    else:
        return diminuicao
    
    
def dobro(valor=0, format=False, moeda="R$"):
    dobro = valor * 2
    if format:
        return f"{moeda}{dobro:.2f}".replace(".", ",")
    else:
        return dobro


def metade(valor=0, format=False, moeda="R$"):
    metade = valor/2
    if format:
        return f"{moeda}{metade:.2f}".replace(".", ",")
    else:
        return metade


def moeda(valor = 0, moeda = "R$"):
    return f"{moeda}{valor:.2f}".replace(".", ",")
    
    
def resumo(valor=0, aumento = 10, reducao = 13):
    print("-"*30)
    print("RESUMO DO VALOR".center(30))
    print("-"*30)
    print(f"Preço analisado: {moeda(valor):>14}")
    print(f"Dobro do preço: {dobro(valor, True):>15}")
    print(f"Metade do preço: {metade(valor, True):>14}")
    print(f"{aumento}% de aumento: {aumentar(valor, aumento, True):>15}")
    print(f"{reducao}% de reduçao: {aumentar(valor, reducao, True):>15}")
    print("-"*30)
    
    
    