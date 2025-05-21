primeiro = int(input("Primeiro termo: "))
razao = int(input("Razao: "))
i = 0
termos = 0
opcao = 1
while opcao != 0:
    while i != 10:
        print(f"{primeiro}", end=" -> ",)
        primeiro += razao
        i +=1
    print("PAUSA")
    opcao = int(input("Quantos termos a mais deseja mostrar? "))
    termos += opcao
    j = 0
    while j != opcao:
        print(f"{primeiro}", end=" -> ")
        primeiro += razao
        j += 1
        
print(f"Progressao finalizada com {termos + 10} termos mostrados")
  