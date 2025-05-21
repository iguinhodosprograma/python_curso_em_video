import math
conta = ""
n = int(input("Digite um numero para calcular seu fatorial: "))
fatorial = math.factorial(n)

while n != 0:
    conta += (f"{n} x " if n > 1 else f"{n}")
    n -= 1
print(f"Calculando {n}! = {conta} = {fatorial}")