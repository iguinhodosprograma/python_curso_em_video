n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))
n3 = int(input("Digite outro numero: "))

if n1 > n2 > n3:
    print(f"o menor numero eh {n3} e o maior eh {n1}")
elif n1 > n3 > n2:
    print(f"o menor numero eh {n2} e o maior eh {n1}")
elif n2 > n1 > n3:
    print(f"o menor numero eh {n3} e o maior eh {n2}")
elif n2 > n3 > n1:
    print(f"o menor numero eh {n1} e o maior eh {n2}")
elif n3 > n1 > n2:
    print(f"o menor numero eh {n2} e o maior eh {n3}")
elif n3 > n2 > n1:
    print(f"o menor numero eh {n1} e o maior eh {n3}")
elif n1 == n2 == n3:
    print("Os numeros sao iguais")