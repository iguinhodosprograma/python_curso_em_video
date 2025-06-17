pessoas = list()
escolha = ""
quant = 0
maiorpeso = 0
menorpeso = 0
maiorpess = list()
menorpess = list()
posi = 0

while escolha in "sS":
    nome = (str(input("Nome: ")))
    peso = (int(input("Peso: ")))
    pessoas.append([nome, peso])
    escolha = str(input("Quer continuar? [S/N] ")).strip().upper()
    while escolha not in "NnSs":
        print("Valor inválido")
        escolha = str(input("Quer continuar? [S/N] ")).strip().upper()
    quant += 1
    
    if len(pessoas) == 1:
        maiorpeso = menorpeso = peso
        maiorpess = [nome]
        menorpess = [nome]
    else:
        if peso == maiorpeso:
            maiorpess.append(nome)
            
        elif maiorpeso < peso:
            maiorpeso = peso
            maiorpess = [nome]       
        
        if peso < menorpeso:
            menorpeso = peso
            menorpess = [nome]
        elif peso == menorpeso:
            menorpess.append(nome)
            
print(f"\nforam cadastradas {len(pessoas)} pessoas")
print(f"O maior peso foi {maiorpeso}Kg. peso de: {maiorpess}")
print(f"O menor peso foi {menorpeso}Kg. peso de: {menorpess}")


        