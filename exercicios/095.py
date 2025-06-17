jogador = {}
time = []
simnao = "s"

total = 0

while simnao in "Ss":
    gols = []
    jogador["nome"] = input("Nome do Jogador: ").capitalize()
    jogador["partidas"] = int(input(f"Quantas partidas {jogador["nome"]} jogou? "))
    for p in range(jogador["partidas"]):
        gol = int(input(f"Quantos gols na partida {p}? "))
        total += gol
        jogador["total"] = total
        gols.append(gol)
        jogador["gols"] = gols
    del(gols)
    time.append(jogador.copy())
    del(jogador["nome"], jogador["partidas"], jogador["gols"], jogador["total"])
    total = 0
    simnao = input("Quer continuar? [S/N] ").upper()
    while simnao not in "NnSs":
        simnao = input("ERRO! Digite apenas S ou N").upper()
    if simnao in "Nn":
        break
j = 1

print("-=" * 30)
print("cod   nome          gols            total")
print("-" * 60)

for jogador in time:
    print(f"{j:<5} {jogador["nome"]:<12} {str (jogador["gols"]):<12} {jogador["total"]:>10}")
    j+=1
print("-" * 60)

escolha = 0
while True:
    jogo = 0
    escolha = int(input("Mostrar dados de qual jogador? (999 para parar) "))
    while escolha > len(time) and escolha != 999:
        print(f"ERRO! Não existe jogador com código {escolha}")
        print("-" * 60)
        escolha = int(input("Mostrar dados de qual jogador? (999 para parar) "))
    if escolha == 999:
        break
    
    jogador = time[escolha - 1]
    print(f"LEVANTAMENTO DO JOGADOR {time[escolha-1]["nome"]}")
    for jogo in range(len(jogador["gols"])):
        print(f"No jogo {jogo + 1} fez {jogador["gols"][jogo]}")
        
print("<< VOLTE SEMPRE >>")