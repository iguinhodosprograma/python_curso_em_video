def titulo(msg):
    tamanho = len(msg) + 4
    print("\033[46m", end="")
    print("~" * tamanho)
    print(f"  {msg}  ")
    print("~" * tamanho)
    print("\033[m")
    
titulo("SISTEMA DE AJUDA PyHELP")
funcao = ""

while funcao != "fim":
    funcao = str(input("Funcão ou Biblioteca > ")).lower().strip()
    titulo(f"Acessando o manual da função {funcao}")
    print("\033[7m")
    print(f"{help(funcao)}")
    print("\033[m")
