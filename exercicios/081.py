lista = []
opcao = ""

while True:
    if opcao == "N":
        break
    n = int(input("Digite um valor: "))
    lista.append(n)
    opcao = (input("Quer continuar? [S/N] ")).upper().strip()
    while opcao not in "NS":
        print("Resposta inválida")
        opcao = (input("Quer continuar? [S/N] ")).upper().strip()
    
print(f"Voce digitou {len(lista)} elementos")

lista.sort(reverse = True)
print(f"Os valores em ordem decrescente são {lista}")

if 5 in lista:
    print("O valor 5 faz parte da lista")
else:
    print("O valor 5 nao faz parte da lista")