frase = str(input("Digite uma frase: ")).upper()
frase = frase.replace(" ", "")
frase2 = frase[::-1]

print(f"Sua frase invertida ficaria: {frase2}")
if frase == frase2:
    print("Isso é um PALINDROMO")
elif frase != frase2:
    print("Isso NAO é um PALINDROMO")
    