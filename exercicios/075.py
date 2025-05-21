n0 = int(input("Digite um valor: "))
n1 = int(input("Digite um valor: "))
n2 = int(input("Digite um valor: "))
n3 = int(input("Digite um valor: "))
lista = (n0, n1, n2, n3)

print(f"O numero 9 apareceu {lista.count(9)} vezes")
if 3 in lista:
    print(f"O primeiro numero 3 apareceu na posicao {lista.index(3)}")
else:
    print("O numero 3 nao foi digitado")
c = 0
print(f"Os numeros pares foram", end=": ")
for c in lista:
    if c % 2 == 0:
        print(c, end = " ")
