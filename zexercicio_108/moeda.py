def aumentar(valor, porcentagem):
    aumento = (valor * (porcentagem/100)) + valor
    return aumento


def diminuir(valor, porcentagem):
    diminuicao = valor - (valor * (porcentagem/100))
    return diminuicao

def dobro(valor):
    return valor*2

def metade(valor):
    return valor/2


def moeda(valor):
    return f"R${valor:.2f}".replace(".", ",")