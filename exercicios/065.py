n1 = int(input("Digite um numero: "))
i = 1
media = 0
maior = menor = n1
cont = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
while cont == "S":
    n = int(input("Digite um numero: "))
    n1 = n + n1
    i += 1
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    cont = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
    if cont == "N":
        print(end="")
    elif cont not in "S":
        print("Resposta inválida.")
        cont = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
media = n1 / i
print(f"Voce digitou {i} numeros e a media foi {media}")
print(f"O maior numero foi {maior} e o menor foi {menor}")



