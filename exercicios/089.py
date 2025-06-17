continuar = ""
boletim = [[]]
a = 0
medias = []

while continuar in "Ss":
    aluno = str(input("Aluno: "))
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    boletim[a].append(aluno)
    boletim[a].append(nota1)
    boletim[a].append(nota2)
    media = (nota1 + nota2)/2
    medias.append(media)
    
    boletim.append([])
    continuar = input("Quer continuar? [S/N]: ")
    while continuar not in "NnSs":
        continuar = input("Resposta invalida. Quer continuar? [S/N]: ")
    a+=1
    
boletim.pop()  
print("-="*30)
p = 0

for p in range(len(boletim)):
    nome = boletim[p][0]
    print(f"{p + 1} {nome} {medias[p]:.1f}")
escolha = 0

while True:
    escolha = int(input("Mostrar notas de qual aluno? (999 interrompe): "))
    while escolha > len(boletim) and escolha != 999:
        escolha = int(input("Valor Incorreto. Mostrar notas de qual aluno? (999 interrompe): "))
        
    if escolha == 999:
        break
    
    print(f"As notas de {boletim[escolha - 1][0]} são {boletim[escolha - 1][1]:.1f} e {boletim[escolha - 1][2]:.1f}")
    

    


    