lista = []
opcao = ""
v = 0
while True:
    if opcao == "N":
        break
    n = int(input("Digite um valor: "))
    
    
    if n not in lista:
        lista.append(n)
        print("Valor adicionado com sucesso...")
    else:
        print("Valor duplicado! Nao vou adicionar")

    opcao = (input("Quer continuar? [S/N] ")).upper().strip()
    while opcao not in "NS":
        print("Resposta inválida")
        opcao = (input("Quer continuar? [S/N] ")).upper().strip()
lista.sort()
print(f"Voce digitou os valores {lista}")
        
