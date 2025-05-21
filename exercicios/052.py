n = int(input("Digite um numero: "))
tot = 0

for c in range(1, n+1):
    if n % c == 0:
        tot += 1
    if n % c == 0:
        print(f"\033[0;33m{c}\033[m", end=" ")
    else:
        print(f"\033[0;31m{c}\033[m", end=" ")

if tot == 2:
    print(f"\nO numero {n} é divisivel somente por 1 e por ele mesmo. ELE É PRIMO")
else:
    print(f"\nO numero {n} NAO é primo")