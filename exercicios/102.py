def fatorial(n, show = False):
    """
    Calcula o fatorial de um numero
    n: o Numero a ser calculado
    show: determina se o calculo é mostrado ou não
    return: O valor do fatorial do numero n
    """
    f = 1
    for c in range(n, 0, -1):
        f*=c
        if show:
            print(c, end="")
            if c>1:
                print(" X ", end="")
            else:
                print(" = ", end="")
    return f

print(fatorial(5))
help(fatorial)