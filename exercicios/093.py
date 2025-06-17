jogador = {}
jogador["nome"] = input("Nome do Jogador: ")
quant = int(input(f"Quantas partidas {jogador["nome"]} jogou? "))
soma = 0
gols = []
for p in range(quant):
    gol = int(input(f"Quantos gols na partida {p + 1}? "))
    soma += gol
    gols.append(gol)
jogador["gols"] = gols
jogador["total"] = soma


print("-="*30)
print(jogador)
print("-="*30)

print(f"O jogador se chama {jogador["nome"]}")
print(f"{jogador["nome"]} fez, separadamente, {gols} gols em cada partida")
print(f"O total de gols foi: {jogador["total"]}")
print("-="*30)

for p in range(quant):
    print(f"=> Na partida {p + 1}, fez {gols[p]} gols")
print(f"Foi um total de {jogador["total"]} gols")

