soma = 0
for c in range (1, 501):
    if c % 3 == 0 and c % 2 != 0:
        soma += c
        cont = cont + 1
print(f"A soma de todos os {cont} valores foi de {soma}")