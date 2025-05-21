lista = ("APRENDER", "PROGRAMAS", "LINGUAGEM", "PYTHON", "CURSO", "GRATIS")

for c in lista:
    print(f"\nNa palavra {c} temos", end= " ")
    for letra in c:
        if letra in "AEIOU":
            print(letra.lower(), end=" ")