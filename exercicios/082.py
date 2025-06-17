lista = []
opcao = ""
imp = []
par = []
while True:
    if opcao == "N":
        break
    n = int(input("Digite um numero: "))
    lista.append(n)
    opcao = (input("Quer continuar? [S/N] ")).upper().strip()
    while opcao not in "NS":
        print("Resposta inválida")
        opcao = (input("Quer continuar? [S/N] ")).upper().strip()
    if n % 2 == 0:
        par.append(n)
    elif n % 2 != 0:
        imp.append(n)
        
print(f"A lista completa é {lista}")
print(f"A lista de pares {par}")
print(f"A lista de impares {imp}")
    