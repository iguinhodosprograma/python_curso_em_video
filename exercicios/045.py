import random
pe = ("""    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
pa = ("""     _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
""")
te = ("""    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

print("""     ██╗ ██████╗ ██╗  ██╗███████╗███╗   ██╗██████╗  ██████╗ 
     ██║██╔═══██╗██║ ██╔╝██╔════╝████╗  ██║██╔══██╗██╔═══██╗
     ██║██║   ██║█████╔╝ █████╗  ██╔██╗ ██║██████╔╝██║   ██║
██   ██║██║   ██║██╔═██╗ ██╔══╝  ██║╚██╗██║██╔═══╝ ██║   ██║
╚█████╔╝╚██████╔╝██║  ██╗███████╗██║ ╚████║██║     ╚██████╔╝
 ╚════╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝╚═╝      ╚═════╝ 
                                                            """)
jogador = int(input("PEDRA(0) PAPEL(1) OU TESOURA(2)? "))
opcoes = [pe, pa, te]
computador = random.randint(0,2)
print(opcoes [jogador])
print("escolha do computador: ")
print(opcoes[computador])

if computador == jogador:
    print("EMPATE")
elif computador == 0 and jogador == 1:
    print("JOGADOR GANHOU")
elif computador == 1 and jogador == 2:
    print("JOGADOR GANHOU")
elif computador == 2 and jogador == 0:
    print("JOGADOR GANHOU")
elif computador == 0 and jogador == 2:
    print("COMPUTADOR GANHOU")
elif computador == 1 and jogador == 0:
    print("COMPUTADOR GANHOU")
elif computador == 2 and jogador == 1:
    print("COMPUTADOR GANHOU")