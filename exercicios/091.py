jogadores = {}
from random import randint
from time import sleep
from operator import itemgetter
jogadores["jogador1"] = randint(1,6)
jogadores["jogador2"] = randint(1,6)
jogadores["jogador3"] = randint(1,6)
jogadores["jogador4"] = randint(1,6)

print("Valores sorteados: ")
for k, v in jogadores.items():
    print(f"O {k} tirou {v} no dado")
    sleep(0.5)
ranking = []
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

print("-=" * 30)

print("RANKING DOS JOGADORES")

for j, d in enumerate(ranking):
    print(f"{j}º Lugar: {d[0]} com {d[1]}")
    sleep(0.5)
