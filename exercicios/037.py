n = int(input("Digite um numero inteiro: "))
escolha = int(input("""Escolha uma das bases para conversao:
    [ 1 ] BINARIO
    [ 2 ] OCTAL
    [ 3 ] HEXADECIMAL
    Sua opçao: """))
if escolha == 1:
    n = bin(n)
    print(n[2:])
elif escolha == 2:
    n = oct(n)
    print(n[2:])
elif escolha == 3:
    n = hex(n)
    print(n[2:])
else:
    print("Escolha somente uma das 3 opçoes")