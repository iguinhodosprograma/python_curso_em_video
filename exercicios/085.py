numeros = [[], []]

 
for i in range(1, 8):
    num = int(input(f"Digite o {i}º numero: "))
    i += 1
    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)
numeros[0].sort()
numeros[1].sort()
print(f"Os numeros pares foram: {numeros[0]}")
print(f"Os numeros impares foram: {numeros[1]}")