import random
r = int(input("Digite um numero de 1 a 5: "))

n = random.randint(1,5)
if r == n:
    print("PARABENS! Voce acertou!")
else:
    print("Voce errou.\n")
    print(f"O numero era {n}")
    
print("Quer jogar novamente!?")