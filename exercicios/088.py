print("-"*40)
print(f"           JOGA NA MEGA SENA")
print("-"*40)

from time import sleep
from random import randint
quant = int(input("Quantos jogos voce quer que eu sorteie? "))
jogos = []
jogo = 0

for lista in range(quant):
    jogos.append([])
    for espaco in range(0,6):
        jogo = randint(1, 60)
        for num in jogos[lista]:
            while jogo == num:
                jogo = randint(1, 60)
        jogos[lista].append(jogo)
        
    lista -= 1
j = 0 

print(f"=-=-=-=   SORTEANDO {quant} JOGOS   =-=-=-=\n")
for j in range(quant):
    print(f"Jogo {j+1}: ", jogos[j], end="")
    print()
    sleep(1)
    j+=1
    
        
