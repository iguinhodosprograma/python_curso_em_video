import random
maior = 0
numeros = tuple(random.randint(1,10) for _ in range (5))

maior = max(numeros)
menor = min(numeros)

print("Os numeros sorteados foram ", end="")
for n in numeros:
    print(f"{n}", end=" ")
print(f"\nO maior valor foi {maior}")
print(f"O menor valor foi {menor}")
