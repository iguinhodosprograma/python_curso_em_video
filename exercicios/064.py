n = 0
i = 0
termos = 0
while n != 999:
    n = int(input("Digite um numero [999 para parar]: "))
    i += n 
    termos += 1
print(f"Voce digitou {termos - 1} numeros e a soma entre eles foi {i - 999}")