print("-=-"*10)
print("VAMOS JOGAR PAR OU IMPAR")
print("-=-"*10)
import random
vitorias = 0
while True:
    player = int(input("Diga um valor: [de 1 ate 10] "))
    escolha = str(input("Par ou Impar? [P/I] ")).upper().strip()[0] 
    computador = random.randint(1,10)
    resultado = computador + player
    
    print(f"Voce jogou {player} e o computador jogou {computador}. Total: {resultado}")
    if (resultado % 2 == 0 and escolha == "P") or (resultado % 2 != 0 and escolha == "I"):
        print("VOCE VENCEU")
        vitorias += 1
        print("Vamos jogar novamente...\n")
    else:
        print("VOCE PERDEU")
        break
print("="*20)
print("GAME OVER")
print(f"Voce venceu um total de {vitorias} partidas")

        
    