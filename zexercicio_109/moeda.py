def aumentar(valor, porcentagem, format=False, moeda="R$"):
    aumento = (valor * (porcentagem/100)) + valor
    
    if format:
        return f"{moeda}{aumento:.2f}".replace(".", ",")
    else:
        return aumento


def diminuir(valor, porcentagem, format=False, moeda="R$"):
    diminuicao = valor - (valor * (porcentagem/100))
    if format:
        return f"{moeda}{diminuicao:.2f}".replace(".", ",")
    else:
        return diminuicao
    
    
def dobro(valor, format=False, moeda="R$"):
    dobro = valor * 2
    if format:
        return f"{moeda}{dobro:.2f}".replace(".", ",")
    else:
        return dobro


def metade(valor, format=False, moeda="R$"):
    metade = valor/2
    if format:
        return f"{moeda}{metade:.2f}".replace(".", ",")
    else:
        return metade


def moeda(valor = 0, moeda = "R$"):
    return f"{moeda}{valor:.2f}".replace(".", ",")