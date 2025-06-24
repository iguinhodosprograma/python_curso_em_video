def leiaint(msg=1):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print("\033[31m ERRO! Digite um número inteiro válido\033[m")
        if ok:
            break
    return valor

n = leiaint("Digite um numero: ")
print(f"Voce acabou de digitar o número {n}")